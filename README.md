# One Line, One Chill

[![make.fun](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/competitions/u-azazex-one-line-one-chill-6d4d5488)
[![Rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/0xyfann/makefun-u-azazex-one-line-one-chill-6d4d5488/rank.svg)](https://make.fun/competitions/u-azazex-one-line-one-chill-6d4d5488)
[![Reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/0xyfann/makefun-u-azazex-one-line-one-chill-6d4d5488/reward.svg)](https://make.fun/competitions/u-azazex-one-line-one-chill-6d4d5488)

A [make.fun](https://make.fun) entry for **One Line, One Chill**
(`u-azazex-one-line-one-chill-6d4d5488`): one sentence of horror, under
200 characters, judged head to head by an AI horror editor on how
frightening, vivid, original, and well-crafted it is.

## The line

> My mother's voicemail ended with her whispering, 'Don't let me in,'
> and then something knocked twice on the door from the inside.

129 characters. One sentence. The voice you trust most warns you
against itself — and the knock comes from the wrong side of the door.

## How it works

`main.py` (Python 3.13, standard library only, no network, fully
deterministic) writes that line to `$MAKEFUN_OUTPUT_DIR/entry.txt`,
validating it against the competition gate first (UTF-8, 1–200
characters, exactly one sentence).

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

See [BUILD-NOTES.md](BUILD-NOTES.md) for the design rationale,
revision history, and local test results.

## License

MIT

---

Built for [make.fun](https://make.fun/r/p1x954ca) — join with my referral link: https://make.fun/r/p1x954ca
