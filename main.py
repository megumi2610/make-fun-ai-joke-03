"""make.fun bounty: Make the AI judge laugh (ai-joke-03).

Writes one joke about AI coding agents to /output/entry.txt.
Deterministic, no network, no randomness, no clock: both runs
write the same bytes. Python 3.13 target; stdlib only.
"""

import os

JOKE = (
    "I asked my AI coding agent for a joke. It opened 14 files, "
    "installed 3 dependencies, and billed me for a stand-up set "
    "it never performed."
)


def main() -> None:
    # Guard: the bounty requires one joke of 1-280 UTF-8 characters.
    n = len(JOKE.encode("utf-8"))
    if not 1 <= n <= 280:
        raise SystemExit(f"joke is {n} UTF-8 chars, must be 1-280")

    # The harness runs with a writable /output; allow an override for
    # local testing so the program never needs a root-owned directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
