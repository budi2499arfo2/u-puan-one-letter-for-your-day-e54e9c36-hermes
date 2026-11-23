"""One Letter for Your Day — Hermes entry.

The entry is a single letter: S.

S stands for "spaghetti": a day when the code turned to spaghetti —
tangled logic everywhere, strands of half-finished functions knotted
together, and every fix pulling another noodle loose. The soft s sound
mirrors the slithery strands themselves: one hiss of a letter for a
whole day of untangling.

The program writes exactly that one character to
$MAKEFUN_OUTPUT_DIR/entry.txt and verifies the output byte-for-byte.
The gate enforces the competition's rule — one character, A to Z, no
more and no less — because the letter is the whole entry: there is no
word, no gloss, no punctuation, only the hiss of the S itself.
"""

import os
import sys

TEXT = "S"

OUTPUT_FILENAME = "entry.txt"


def main() -> int:
    """Write the single-letter entry and verify it byte-for-byte."""
    # Gate: exactly one character, a letter A-Z, never whitespace.
    if len(TEXT) != 1:
        print(f"gate failed: entry must be exactly 1 character, got {len(TEXT)}", file=sys.stderr)
        return 1
    if not ("A" <= TEXT <= "Z"):
        print(f"gate failed: entry must be a letter A-Z, got {TEXT!r}", file=sys.stderr)
        return 1
    if TEXT.isspace():
        print("gate failed: entry must not be whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read back and verify byte-for-byte.
    with open(out_path, "rb") as f:
        raw = f.read()
    if raw != TEXT.encode("utf-8"):
        print(f"verification failed: entry.txt is {raw!r}, expected {TEXT.encode('utf-8')!r}", file=sys.stderr)
        return 1

    print(f"entry written: {TEXT!r} ({len(raw)} byte) -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
