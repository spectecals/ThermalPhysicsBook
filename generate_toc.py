#!/usr/bin/env python3
# gen_toc.py
from __future__ import annotations
import argparse
from pathlib import Path
import yaml

PREFERRED_ROOTS = (
    "index.md", "index.ipynb", "README.md", "README.ipynb",
)

def rel_no_ext(p: Path, root: Path) -> str:
    return p.relative_to(root).as_posix().removesuffix(".ipynb").removesuffix(".md")

def find_notebooks(root: Path) -> list[Path]:
    # Ignore typical junk
    ignore_dirs = {".git", ".hg", ".svn", ".eggs", ".mypy_cache", ".pytest_cache",
                   ".ipynb_checkpoints", ".venv", "venv", "__pycache__", "_build", ".dvc"}
    notebooks = []
    for p in root.rglob("*.ipynb"):
        parts = set(p.parts)
        if parts & ignore_dirs:
            continue
        if p.name.endswith("-checkpoint.ipynb"):
            continue
        if p.name.startswith("_"):  # often project-local meta pages; exclude if you want them, remove this
            continue
        notebooks.append(p)
    return sorted(notebooks, key=lambda q: q.relative_to(root).as_posix())

def choose_root(root: Path, notebooks: list[Path]) -> Path:
    # Prefer a conventional root if it exists; fall back to first notebook.
    for candidate in PREFERRED_ROOTS:
        cp = root / candidate
        if cp.exists():
            return cp
    if not notebooks:
        raise SystemExit("No notebooks found; cannot build _toc.yml")
    return notebooks[0]

def build_toc(root: Path, notebooks: list[Path], chosen_root: Path) -> dict:
    # Jupyter Book expects 'format' and 'root'. We’ll produce a flat 'chapters' list in path order.
    root_rel = rel_no_ext(chosen_root, root)
    # remove the root from chapters if it’s a notebook and present in notebooks
    chapters = [
        {"file": rel_no_ext(nb, root)}
        for nb in notebooks
        if nb.resolve() != chosen_root.resolve()
    ]
    return {
        "format": "jb-book",
        "root": root_rel,
        "options": { "numbered": True },
        "chapters": chapters,
    }

def main() -> None:
    ap = argparse.ArgumentParser(description="Generate _toc.yml for Jupyter Book by alphabetically sorted notebook paths.")
    ap.add_argument("--book-root", default=".", help="Path to the book root (where _config.yml lives). Default: .")
    ap.add_argument("--outfile", default="_toc.yml", help="Output filename. Default: _toc.yml")
    ap.add_argument("--include-underscore", action="store_true",
                    help="Include files/dirs starting with '_' (by default they’re excluded).")
    args = ap.parse_args()

    root = Path(args.book_root).resolve()
    if not root.exists():
        raise SystemExit(f"Book root not found: {root}")

    notebooks = find_notebooks(root)
    # # Explicitly remove index.ipynb so it never becomes a chapter
    # notebooks = [nb for nb in notebooks if nb.name not in PREFERRED_ROOTS]

    if args.include_underscore:
        # re-run including underscore files
        def find_all(root: Path) -> list[Path]:
            ignore_dirs = {".git", ".hg", ".svn", ".eggs", ".mypy_cache", ".pytest_cache",
                           ".ipynb_checkpoints", ".venv", "venv", "__pycache__", "_build", ".dvc"}
            res = []
            for p in root.rglob("*.ipynb"):
                parts = set(p.parts)
                if parts & ignore_dirs:
                    continue
                if p.name.endswith("-checkpoint.ipynb"):
                    continue
                res.append(p)
            return sorted(res, key=lambda q: q.relative_to(root).as_posix())
        notebooks = find_all(root)

    chosen_root = choose_root(root, notebooks)
    toc = build_toc(root, notebooks, chosen_root)

    # Dump YAML with stable ordering and no aliases
    class NoAliasDumper(yaml.SafeDumper):
        def ignore_aliases(self, data):
            return True

    out_path = root / args.outfile
    with out_path.open("w", encoding="utf-8") as f:
        yaml.dump(toc, f, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True)

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
