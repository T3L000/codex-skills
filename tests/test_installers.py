from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
POWERSHELL_INSTALLER = REPO_ROOT / "scripts" / "install-skill.ps1"
SHELL_INSTALLER = REPO_ROOT / "scripts" / "install-skill.sh"


def has_usable_bash() -> bool:
    bash = shutil.which("bash")
    if not bash:
        return False
    result = subprocess.run(
        [bash, "--version"],
        capture_output=True,
        timeout=10,
    )
    return result.returncode == 0


class PowerShellInstallerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.destination = Path(self.temp_dir.name) / "skills"

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def run_installer(
        self,
        name: str,
        *extra: str,
        installer: Path = POWERSHELL_INSTALLER,
        cwd: Path = REPO_ROOT,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(installer),
                "-Name",
                name,
                "-Destination",
                str(self.destination),
                *extra,
            ],
            cwd=cwd,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
        )

    def test_installs_recommended_vendored_skill(self) -> None:
        result = self.run_installer("mcp-builder")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue((self.destination / "mcp-builder" / "SKILL.md").is_file())

    def test_rejects_unknown_traversal_deprecated_and_external_skills(self) -> None:
        for name in ("missing-skill", "../mcp-builder", "brainstorming", "kimi-webbridge"):
            with self.subTest(name=name):
                result = self.run_installer(name)
                self.assertNotEqual(0, result.returncode)

    def test_refuses_overwrite_without_force_and_allows_explicit_force(self) -> None:
        first = self.run_installer("project-memory")
        self.assertEqual(0, first.returncode, first.stderr)
        marker = self.destination / "project-memory" / "marker.txt"
        marker.write_text("old", encoding="utf-8")

        refused = self.run_installer("project-memory")
        self.assertNotEqual(0, refused.returncode)
        self.assertTrue(marker.exists())

        forced = self.run_installer("project-memory", "-Force")
        self.assertEqual(0, forced.returncode, forced.stderr)
        self.assertFalse(marker.exists())

    def test_installs_from_unicode_repository_path(self) -> None:
        unicode_repo = Path(self.temp_dir.name) / "中文技能仓库"
        scripts_dir = unicode_repo / "scripts"
        catalog_dir = unicode_repo / "catalog"
        skill_dir = unicode_repo / "skills" / "sample-skill"
        scripts_dir.mkdir(parents=True)
        catalog_dir.mkdir()
        skill_dir.mkdir(parents=True)

        shutil.copy2(POWERSHELL_INSTALLER, scripts_dir / "install-skill.ps1")
        shutil.copy2(
            REPO_ROOT / "scripts" / "validate-catalog.py",
            scripts_dir / "validate-catalog.py",
        )
        (skill_dir / "SKILL.md").write_text(
            "---\nname: sample-skill\ndescription: Unicode path fixture\n---\n",
            encoding="utf-8",
        )
        (catalog_dir / "skills.yaml").write_text(
            """\
schema_version: 1
skills:
  - id: sample-skill
    name: Sample Skill
    category: testing
    distribution: vendored
    purpose: 验证中文仓库路径安装。
    upstream: https://example.com/sample-skill
    install:
      repository: install sample-skill
    license: MIT
    status: recommended
    risk_notes: 仅用于测试。
    verified_on: "2026-07-29"
""",
            encoding="utf-8",
        )

        result = self.run_installer(
            "sample-skill",
            installer=scripts_dir / "install-skill.ps1",
            cwd=unicode_repo,
        )

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue((self.destination / "sample-skill" / "SKILL.md").is_file())


@unittest.skipUnless(
    has_usable_bash(),
    "当前环境没有可用 bash（Windows WSL 占位程序不算），跳过 POSIX shell 安装器测试。",
)
class ShellInstallerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.destination = Path(self.temp_dir.name) / "skills"

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def run_installer(self, name: str, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                "bash",
                str(SHELL_INSTALLER),
                name,
                "--destination",
                str(self.destination),
                *extra,
            ],
            cwd=REPO_ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
        )

    def test_installs_recommended_vendored_skill(self) -> None:
        result = self.run_installer("scouting-ai-ecosystem")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue(
            (self.destination / "scouting-ai-ecosystem" / "SKILL.md").is_file()
        )

    def test_rejects_traversal_and_external_skill(self) -> None:
        for name in ("../../mcp-builder", "deep-research"):
            with self.subTest(name=name):
                result = self.run_installer(name)
                self.assertNotEqual(0, result.returncode)

    def test_force_replaces_existing_directory(self) -> None:
        first = self.run_installer("project-memory")
        self.assertEqual(0, first.returncode, first.stderr)
        marker = self.destination / "project-memory" / "marker.txt"
        marker.write_text("old", encoding="utf-8")

        refused = self.run_installer("project-memory")
        self.assertNotEqual(0, refused.returncode)
        self.assertTrue(marker.exists())

        forced = self.run_installer("project-memory", "--force")
        self.assertEqual(0, forced.returncode, forced.stderr)
        self.assertFalse(marker.exists())


if __name__ == "__main__":
    unittest.main()
