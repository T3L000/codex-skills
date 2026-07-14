from __future__ import annotations

import importlib.util
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate-catalog.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_catalog", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载目录校验器：{VALIDATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ValidateCatalogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = load_validator()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_root = Path(self.temp_dir.name)
        (self.repo_root / "catalog").mkdir()
        (self.repo_root / "skills" / "sample-skill").mkdir(parents=True)
        (self.repo_root / "skills" / "sample-skill" / "SKILL.md").write_text(
            "---\nname: sample-skill\ndescription: 示例\n---\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_catalog(self, body: str) -> Path:
        catalog_path = self.repo_root / "catalog" / "skills.yaml"
        catalog_path.write_text(textwrap.dedent(body).lstrip(), encoding="utf-8")
        return catalog_path

    def valid_record(self, **overrides: str) -> dict[str, object]:
        record: dict[str, object] = {
            "id": "sample-skill",
            "name": "Sample Skill",
            "category": "workflow",
            "distribution": "vendored",
            "purpose": "用于测试目录校验。",
            "upstream": "https://example.com/sample-skill",
            "install": {"repository": "./scripts/install-skill.ps1 -Name sample-skill"},
            "license": "MIT",
            "status": "recommended",
            "risk_notes": "仅复制本地文件。",
            "verified_on": "2026-07-14",
        }
        record.update(overrides)
        return record

    def write_records(self, records: list[dict[str, object]]) -> Path:
        import yaml

        path = self.repo_root / "catalog" / "skills.yaml"
        path.write_text(
            yaml.safe_dump({"skills": records}, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
        return path

    def test_valid_catalog_passes(self) -> None:
        path = self.write_records([self.valid_record()])
        self.assertEqual([], self.validator.validate_catalog(self.repo_root, path))

    def test_missing_required_field_is_reported_with_record(self) -> None:
        record = self.valid_record()
        del record["purpose"]
        path = self.write_records([record])

        errors = self.validator.validate_catalog(self.repo_root, path)

        self.assertTrue(any("sample-skill" in error and "purpose" in error for error in errors))

    def test_duplicate_id_is_rejected(self) -> None:
        path = self.write_records([self.valid_record(), self.valid_record()])

        errors = self.validator.validate_catalog(self.repo_root, path)

        self.assertTrue(any("重复" in error and "sample-skill" in error for error in errors))

    def test_unknown_status_is_rejected(self) -> None:
        path = self.write_records([self.valid_record(status="abandoned")])

        errors = self.validator.validate_catalog(self.repo_root, path)

        self.assertTrue(any("status" in error and "abandoned" in error for error in errors))

    def test_deprecated_requires_replacement_information(self) -> None:
        path = self.write_records([self.valid_record(status="deprecated")])

        errors = self.validator.validate_catalog(self.repo_root, path)

        self.assertTrue(any("deprecated" in error and "replacement" in error for error in errors))

    def test_vendored_skill_requires_skill_file(self) -> None:
        record = self.valid_record(id="missing-skill")
        path = self.write_records([record])

        errors = self.validator.validate_catalog(self.repo_root, path)

        self.assertTrue(any("missing-skill" in error and "SKILL.md" in error for error in errors))

    def test_unknown_distribution_is_rejected(self) -> None:
        path = self.write_records([self.valid_record(distribution="remote")])

        errors = self.validator.validate_catalog(self.repo_root, path)

        self.assertTrue(any("distribution" in error and "remote" in error for error in errors))

    def test_replacement_target_must_exist(self) -> None:
        path = self.write_records(
            [
                self.valid_record(
                    status="deprecated",
                    replaced_by="missing-replacement",
                    replacement_reason="使用新实现。",
                )
            ]
        )

        errors = self.validator.validate_catalog(self.repo_root, path)

        self.assertTrue(
            any("replaced_by" in error and "missing-replacement" in error for error in errors)
        )


class RepositoryCatalogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = load_validator()
        self.catalog_path = REPO_ROOT / "catalog" / "skills.yaml"

    def load_records(self) -> list[dict[str, object]]:
        import yaml

        data = yaml.safe_load(self.catalog_path.read_text(encoding="utf-8"))
        return data["skills"]

    def test_repository_catalog_is_valid(self) -> None:
        self.assertEqual(
            [],
            self.validator.validate_catalog(REPO_ROOT, self.catalog_path),
        )

    def test_repository_catalog_covers_original_skills(self) -> None:
        original_ids = {
            "brainstorming",
            "code-review-and-quality",
            "docx",
            "drawio-skill",
            "hatch-pet",
            "mcp-builder",
            "planning-with-files",
            "ppt-master",
            "project-memory",
            "systematic-debugging",
            "test-driven-development",
            "ui-ux-pro-max",
            "using-superpowers",
            "verification-before-completion",
            "webapp-testing",
            "web-design-guidelines",
            "writing-plans",
            "xlsx",
        }
        catalog_ids = {str(record["id"]) for record in self.load_records()}
        self.assertTrue(original_ids <= catalog_ids)

    def test_repository_catalog_has_external_and_replacement_records(self) -> None:
        records = self.load_records()
        self.assertTrue(any(record["distribution"] == "external" for record in records))
        self.assertTrue(
            any(record.get("replaced_by") for record in records),
            "目录应显式记录至少一项替代关系。",
        )


if __name__ == "__main__":
    unittest.main()
