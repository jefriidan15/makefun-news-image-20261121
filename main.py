#!/usr/bin/env python3
"""Write the news-image-20261121 entry to $MAKEFUN_OUTPUT_DIR/entry.png.

The front-page image is drawn once and shipped in this repository as
entry.png; this program only copies it to the output directory and
checks the copy is byte-identical. Standard library only, no network.
"""
import hashlib
import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    with open(source, "rb") as fh:
        data = fh.read()
    if data[:8] != PNG_MAGIC:
        print("entry.png does not start with the PNG magic bytes",
              file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    with open(target, "rb") as fh:
        written = fh.read()
    if written[:8] != PNG_MAGIC:
        print("written entry.png does not start with the PNG magic bytes",
              file=sys.stderr)
        return 1
    if written != data or hashlib.sha256(written).hexdigest() != digest:
        print("written entry.png does not match the source",
              file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(written)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
