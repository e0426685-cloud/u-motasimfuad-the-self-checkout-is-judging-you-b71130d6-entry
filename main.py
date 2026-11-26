"""The Self-Checkout Is Judging You - make.fun one-line entry.

Writes a single funny line in the voice of a smug self-checkout machine
to /output/entry.txt. Python standard library only.
"""

import os

ENTRY = "Twelve yogurts and zero actual food \u2014 don't worry, I'll ring it up as groceries so you can keep calling it a meal plan."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main():
    line = ENTRY
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    if len(line.encode("utf-8")) > MAX_CHARS * 4:
        raise ValueError("entry exceeds the UTF-8 size budget")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    # Round-trip check: what the grader reads must be exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError("round-trip mismatch: entry.txt does not match ENTRY")


if __name__ == "__main__":
    main()
