#!/usr/bin/env python3
"""校验 catalog/skills.yaml 的结构和仓库内 Skill 引用。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml


REQUIRED_FIELDS = (
    "id",
    "name",
    "category",
    "distribution",
    "purpose",
    "upstream",
    "install",
    "license",
    "status",
    "risk_notes",
    "verified_on",
)
VALID_DISTRIBUTIONS = {"vendored", "external"}
VALID_STATUSES = {"recommended", "maintained", "deprecated", "unverified"}


def _label(record: dict[str, Any], index: int) -> str:
    return str(record.get("id") or f"第 {index + 1} 条记录")


def _is_empty(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def validate_catalog(repo_root: Path, catalog_path: Path) -> list[str]:
    """返回全部校验错误；空列表表示目录有效。"""

    errors: list[str] = []
    try:
        data = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"目录文件不存在：{catalog_path}"]
    except yaml.YAMLError as exc:
        return [f"YAML 解析失败：{exc}"]

    if not isinstance(data, dict) or not isinstance(data.get("skills"), list):
        return ["目录根节点必须是包含 skills 列表的对象。"]

    seen_ids: set[str] = set()
    for index, raw_record in enumerate(data["skills"]):
        if not isinstance(raw_record, dict):
            errors.append(f"第 {index + 1} 条记录必须是对象。")
            continue

        record: dict[str, Any] = raw_record
        label = _label(record, index)
        for field in REQUIRED_FIELDS:
            if field not in record or _is_empty(record[field]):
                errors.append(f"{label}：缺少必填字段 {field}。")

        skill_id = record.get("id")
        if isinstance(skill_id, str) and skill_id:
            if skill_id in seen_ids:
                errors.append(f"{label}：发现重复 id：{skill_id}。")
            seen_ids.add(skill_id)

        distribution = record.get("distribution")
        if distribution not in VALID_DISTRIBUTIONS:
            errors.append(
                f"{label}：distribution={distribution!r} 无效，"
                f"可选值为 {sorted(VALID_DISTRIBUTIONS)}。"
            )
        elif distribution == "vendored" and isinstance(skill_id, str):
            skill_file = repo_root / "skills" / skill_id / "SKILL.md"
            if not skill_file.is_file():
                errors.append(f"{label}：vendored Skill 缺少 {skill_file.relative_to(repo_root)}。")

        status = record.get("status")
        if status not in VALID_STATUSES:
            errors.append(
                f"{label}：status={status!r} 无效，可选值为 {sorted(VALID_STATUSES)}。"
            )
        elif status == "deprecated" and not (
            record.get("replaced_by") or record.get("replacement_reason")
        ):
            errors.append(
                f"{label}：deprecated 记录必须填写 replaced_by 或 replacement_reason。"
            )

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "catalog",
        nargs="?",
        default="catalog/skills.yaml",
        type=Path,
        help="待校验的目录文件（默认：catalog/skills.yaml）",
    )
    args = parser.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    catalog_path = args.catalog
    if not catalog_path.is_absolute():
        catalog_path = Path.cwd() / catalog_path

    errors = validate_catalog(repo_root, catalog_path.resolve())
    if errors:
        print("Skill 目录校验失败：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Skill 目录有效：{catalog_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
