#!/usr/bin/env python3
"""校验 catalog/skills.yaml 的结构和仓库内 Skill 引用。"""

from __future__ import annotations

import argparse
import re
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
INSTALLABLE_STATUSES = {"recommended", "maintained"}
SKILL_ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


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
    records: list[dict[str, Any]] = []
    for index, raw_record in enumerate(data["skills"]):
        if not isinstance(raw_record, dict):
            errors.append(f"第 {index + 1} 条记录必须是对象。")
            continue

        record: dict[str, Any] = raw_record
        records.append(record)
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

    for index, record in enumerate(records):
        replacement = record.get("replaced_by")
        if replacement and replacement not in seen_ids:
            errors.append(
                f"{_label(record, index)}：replaced_by 指向不存在的记录 {replacement!r}。"
            )

    return errors


def resolve_installable_skill(
    repo_root: Path, catalog_path: Path, skill_id: str
) -> tuple[Path | None, str | None]:
    """解析允许由本仓库安装的 Skill，并返回安全的绝对源路径。"""

    if not SKILL_ID_PATTERN.fullmatch(skill_id):
        return None, "Skill ID 只能包含小写字母、数字和连字符。"

    errors = validate_catalog(repo_root, catalog_path)
    if errors:
        return None, "目录无效，拒绝安装：" + "；".join(errors)

    data = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    record = next((item for item in data["skills"] if item["id"] == skill_id), None)
    if record is None:
        return None, f"目录中不存在 Skill：{skill_id}。"
    if record["distribution"] != "vendored":
        return None, f"{skill_id} 是外部 Skill，请使用目录中的官方安装方式。"
    if record["status"] not in INSTALLABLE_STATUSES:
        return None, f"{skill_id} 当前状态为 {record['status']}，仓库安装器拒绝安装。"

    skills_root = (repo_root / "skills").resolve()
    source = (skills_root / skill_id).resolve()
    try:
        source.relative_to(skills_root)
    except ValueError:
        return None, "解析后的 Skill 路径越过仓库 skills 目录。"
    if not (source / "SKILL.md").is_file():
        return None, f"{skill_id} 缺少 SKILL.md。"
    return source, None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "catalog",
        nargs="?",
        default="catalog/skills.yaml",
        type=Path,
        help="待校验的目录文件（默认：catalog/skills.yaml）",
    )
    parser.add_argument(
        "--resolve",
        metavar="SKILL_ID",
        help="输出允许安装的仓库内 Skill 绝对路径；不可安装时退出 1。",
    )
    args = parser.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    catalog_path = args.catalog
    if not catalog_path.is_absolute():
        catalog_path = Path.cwd() / catalog_path

    catalog_path = catalog_path.resolve()
    if args.resolve:
        source, error = resolve_installable_skill(repo_root, catalog_path, args.resolve)
        if error:
            print(error, file=sys.stderr)
            return 1
        print(source)
        return 0

    errors = validate_catalog(repo_root, catalog_path)
    if errors:
        print("Skill 目录校验失败：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Skill 目录有效：{catalog_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
