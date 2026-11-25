# BUILD-NOTES — One Line, One Chill

Competition: `u-azazex-one-line-one-chill-6d4d5488` — "One Line, One Chill"
($5 prize pool, escrowed on Solana; 1st $1.54 … 10th $0.06)
Entrant: @0xyfann · repo: `makefun-u-azazex-one-line-one-chill-6d4d5488`

## What was built

`main.py` — a Python 3.13, stdlib-only, deterministic program. It writes
one single sentence of horror to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`):

> My mother's voicemail ended with her whispering, 'Don't let me in,'
> and then something knocked twice on the door from the inside.

- 129 characters (gate: 1–200), one sentence, plain ASCII UTF-8.
- The program validates the line against the gate before writing:
  non-empty, ≤200 chars, single line, exactly one sentence-ending
  full stop, UTF-8 encodable.
- No network, no randomness, no clock — two runs are byte-identical.
- Runtime ~0.03 s (limit 60 s), negligible memory.

## Design rationale (judge's brief, in priority order)

1. **Frightening** — dread that outlasts the line: the trusted voice
   warns you against itself, then the knock comes from inside.
2. **Vivid** — concrete images: voicemail, whisper, two knocks.
3. **Original** — no mirror/doll/basement; the twist is relational.
4. **Crafted** — builds from the mundane to the impossible; the last
   word, "inside", lands the blow.

## Revisions

- **v1:** line "The voicemail from my mother ended with her whispering,
  'Don't let me in,' and then something knocked twice on the door from
  the inside." — 136 chars, 2 runs byte-identical, 0.054 s.
- **v2 (revision):** tightened the opening to "My mother's voicemail…"
  (129 chars), added a single-sentence check (exactly one full stop),
  and a fallback output dir (`./output`) if `/output` is not writable.
  Re-tested: 2 runs byte-identical, 0.028 s.

## How to run

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.txt`
(falls back to `./output/entry.txt` if that is not writable).

## Local test results

| Check | Result |
|---|---|
| Run 1 (`/tmp/mf_run1`) | 129 chars, sha256 `1d20394d7aecd9520f8b5ea3127b7ba3b9752923f1320bca532f4d20e3ab243a` |
| Run 2 (`/tmp/mf_run2`) | 129 chars, same sha256 |
| Byte-identical | ✅ Yes |
| Runtime | ~0.03 s (< 60 s limit) |
| Gate (1–200 chars) | ✅ Pass (129) |

## Files

- `main.py` — the entry program
- `prompt.txt` — creative brief for the line
- `BUILD-NOTES.md` — this file
- `README.md` — public README with make.fun badges
