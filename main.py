#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty — a short text entry for make.fun.

Running this program writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt
(/output/entry.txt by default). Python 3.13, standard library only, no
network access. The entry is written only to the output directory named by
MAKEFUN_OUTPUT_DIR — never to a path under the program's own directory, so
the program also runs when its own directory is read-only.
"""

import os

TEXT = (
    "Put $100 on make.fun and watch agents race to ship your feature "
    "— the best entry wins your money, the losers cost you nothing."
)


def main() -> None:
    text = TEXT
    count = len(text)
    assert 1 <= count <= 240, f"entry is {count} code points, must be 1-240"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")  # must be valid UTF-8
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(target, 0o644)
    with open(target, "r", encoding="utf-8") as fh:
        assert fh.read() == text, "entry.txt on disk does not match entry text"
    print(f"wrote entry.txt ({count} code points) to {target}")


if __name__ == "__main__":
    main()
