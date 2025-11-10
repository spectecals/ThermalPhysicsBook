import json, pathlib
for p in pathlib.Path('.').rglob('*.ipynb'):
    nb = json.loads(p.read_text(encoding='utf-8'))
    changed = False
    for c in nb.get("cells", []):
        if c.get("cell_type") == "code":
            tags = c.setdefault("metadata", {}).setdefault("tags", [])
            if "remove-input" not in tags:
                tags.append("remove-input")
                changed = True
    if changed:
        p.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
        print("tagged", p)