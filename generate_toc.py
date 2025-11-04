#!/usr/bin/env python3
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent
ROOT_NAME = "index.ipynb"
EXCLUDE_DIRS = {"_build", ".git", ".ipynb_checkpoints", "node_modules", ".venv", "venv"}


def is_excluded(p: Path) -> bool:
    return any(part in EXCLUDE_DIRS for part in p.parts)


# collect ipynb files
ipynbs = []
for p in REPO_ROOT.rglob("*.ipynb"):
    if is_excluded(p):
        continue
    ipynbs.append(p.relative_to(REPO_ROOT))

# alphabetical by full path
ipynbs = sorted(ipynbs, key=lambda x: x.as_posix().lower())

# detect root
root = None
for p in ipynbs:
    if p.name.lower() == ROOT_NAME.lower():
        root = p
        break

toc = {
    "format": "jb-book",
    "root": root.with_suffix("").as_posix() if root else ROOT_NAME[:-6],
    "options": {"numbered": 2},
    "chapters": []
}

last_chapter = None

for p in ipynbs:
    if root and p == root:
        continue

    stem = p.stem.lower()
    path_no_ext = p.with_suffix("").as_posix()

    if stem.endswith("_questions"):
        # attach to last chapter as a section
        if last_chapter is None:
            raise ValueError(f"{p} appears to be a questions file, but no chapter precedes it.")
        last_chapter.setdefault("sections", []).append({"file": path_no_ext})
    else:
        # new chapter
        chapter = {"file": path_no_ext}
        toc["chapters"].append(chapter)
        last_chapter = chapter

out_path = REPO_ROOT / "_toc.yml"
with out_path.open("w", encoding="utf-8") as f:
    yaml.safe_dump(toc, f, sort_keys=False, allow_unicode=True)

print(f"Wrote {out_path}")
if not root:
    print("WARNING: index.ipynb not found. Create it to prevent build errors.")
