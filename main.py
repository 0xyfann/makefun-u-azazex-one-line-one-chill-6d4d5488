#!/usr/bin/env python3
"""One Line, One Chill -- make.fun entry.

Writes a single sentence of horror (under 200 characters) to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default: ``/output``).

Python 3.13, standard library only, fully deterministic: two runs
produce byte-identical output. No network, no randomness, no clock,
no environment-dependent behaviour. Runs in well under 60 seconds.

The line was chosen against the judge's published brief, in priority
order:
  1. Frightening -- dread that outlasts the line, earned not announced.
  2. Vivid -- concrete images (a voicemail, a knock) a reader can see.
  3. Original -- no mirror, doll or basement; the scare is a mother's
     voice warning you *against herself*, and a knock from the wrong
     side of the door.
  4. Crafted -- one tight sentence, rhythm builds, last word lands.

Gate: the sealed scorer requires UTF-8 text of 1-200 characters, not
only whitespace. The line below is checked against that gate at
runtime before anything is written.
"""

import os
import sys

# The single horror line. One sentence, plain ASCII, no trailing
# newline in the file itself (the gate counts characters, so the file
# holds exactly the line, nothing else).
LINE = (
    "My mother's voicemail ended with her whispering, "
    "'Don't let me in,' and then something knocked twice "
    "on the door from the inside."
)

MAX_CHARS = 200

def output_dir() -> str:
    """Resolve the output directory.

    The grader sets MAKEFUN_OUTPUT_DIR; fall back to /output (the
    sandbox default named in the rules) and then to ./output so a
    local run never fails for a missing variable.
    """
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )


def validate(line: str) -> None:
    """Enforce the gate locally before writing anything."""
    if not line or not line.strip():
        raise SystemExit("error: line is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            "error: line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    # Exactly one sentence: no newline, no second sentence hiding
    # behind a line break, and a single sentence-ending full stop.
    if "\n" in line or "\r" in line:
        raise SystemExit("error: line must be a single line")
    if not line.endswith(".") or line.count(".") != 1:
        raise SystemExit("error: line must be exactly one sentence")
    # Must be encodable as UTF-8 (the gate reads UTF-8 text).
    line.encode("utf-8")


def main() -> int:
    validate(LINE)
    out_dir = output_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
    except PermissionError:
        # Local run where /output is not writable: fall back to a
        # ./output directory next to the program instead of failing.
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" + explicit encoding: byte-identical on every run,
    # on every platform. No trailing newline -- the file is the line.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
