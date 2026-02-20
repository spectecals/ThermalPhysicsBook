import json, pathlib, re

tag_re = re.compile(r'\\tag\{([^}]+)\}')
close_eq_re = re.compile(r'\$\$')

for p in pathlib.Path('.').rglob('*.ipynb'):
    nb = json.loads(p.read_text(encoding='utf-8'))
    changed = False

    for c in nb.get("cells", []):
        if c.get("cell_type") != "markdown":
            continue

        src = "".join(c.get("source", []))
        out = src
        offset = 0

        for m in tag_re.finditer(src):
            tag = m.group(1)
            start = m.end()

            close = close_eq_re.search(src, start)
            if not close:
                continue

            # remove \tag{x}
            out = (
                out[:m.start() - offset]
                + out[m.end() - offset:]
            )
            offset += m.end() - m.start()

            # insert (x) after the closing $$
            insert_at = close.end() - offset
            out = (
                out[:insert_at]
                + f" ({tag})"
                + out[insert_at:]
            )
            offset -= len(f" ({tag})")

            changed = True

        if out != src:
            c["source"] = [out]

    if changed:
        p.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
        print("rewrote", p)