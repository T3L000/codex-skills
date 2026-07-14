#!/bin/sh
set -eu

usage() {
  echo "用法: $0 <skill-id> [--destination <path>] [--force]" >&2
  exit 2
}

[ "$#" -ge 1 ] || usage
name=$1
shift
destination="${CODEX_HOME:-$HOME/.codex}/skills"
force=0

case "$name" in
  *[!a-z0-9-]* | -* | *- | *--*)
    echo "Skill ID 只能包含小写字母、数字和单个连字符。" >&2
    exit 1
    ;;
esac

while [ "$#" -gt 0 ]; do
  case "$1" in
    --destination)
      [ "$#" -ge 2 ] || usage
      destination=$2
      shift 2
      ;;
    --force)
      force=1
      shift
      ;;
    *)
      usage
      ;;
  esac
done

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd)
catalog="$repo_root/catalog/skills.yaml"

if command -v python3 >/dev/null 2>&1; then
  python_cmd=python3
elif command -v python >/dev/null 2>&1; then
  python_cmd=python
else
  echo "需要 Python 3 和 PyYAML 才能读取安全安装目录。" >&2
  exit 1
fi

if ! source_path=$($python_cmd "$script_dir/validate-catalog.py" "$catalog" --resolve "$name"); then
  exit 1
fi

target="$destination/$name"
mkdir -p -- "$destination"
if [ -e "$target" ]; then
  if [ "$force" -ne 1 ]; then
    echo "目标已存在：$target。若确认替换，请显式使用 --force。" >&2
    exit 1
  fi
  rm -rf -- "$target"
fi

cp -R -- "$source_path" "$target"
echo "已安装 $name 到 $target"
