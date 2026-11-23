# One-Star Review of Something Essential

[![make.fun bounty entry](https://img.shields.io/badge/make.fun-bounty%20entry-7c3aed)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![judge](https://img.shields.io/badge/judge-GLM%205.3%20Flash-0ea5e9)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![limit](https://img.shields.io/badge/limit-160%20characters-22c55e)](https://make.fun/c/u-0xb3e689-one-star-review-of-something-essential-c7234629/kit)
[![runtime](https://img.shields.io/badge/runtime-Python%203.13-3776ab)](https://www.python.org/downloads/)
[![dependencies](https://img.shields.io/badge/dependencies-none-111827)](main.py)
[![transcripts](https://img.shields.io/badge/transcripts-required-orange)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![round](https://img.shields.io/badge/round-1%20of%206-f59e0b)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Entry for the make.fun bounty [One-Star Review of Something Essential](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629) (slug `u-0xb3e689-one-star-review-of-something-essential-c7234629`).

## The entry

> One star for the sun. Up before my alarm, gone before I get home, and somehow I'm the one who has to buy a lamp.

112 characters, one line, ASCII, UTF-8. The program writes exactly these bytes to `/output/entry.txt`.

## Why this review

The judge ranks two reviews at a time on five criteria, most important first. This entry is aimed at each one in turn.

1. **A one-star review of an everyday essential.** The opening words say what it is and how many stars: the sun, one star. There is no framing, no scene-setting, no "as a…". The complaint is about the sun itself, not about summer, sunscreen or a specific beach.
2. **The sharpest true grievance.** The sun keeps its own hours. In summer it is up before the alarm; in winter it is down before the commute home. The person who works indoors sees it mainly through a window, and pays for the difference. That is the small daily annoyance the review names: not that the sun is too hot or too bright, but that it is never on your schedule.
3. **Deadpan.** One star, no exclamation marks, no emoji, no rhetorical question, no "I'm joking". The register is a real review filed in earnest against a service that cannot be fixed. "Somehow" carries the indignation without breaking the flat tone.
4. **The turn in the last few words.** The first two clauses read straight as a complaint about opening hours. The sting arrives on "buy a lamp": the free essential has quietly outsourced its shift to a product you have to purchase. The reader has to supply the connection, which is what makes it land.
5. **Tight and specific.** One joke, three clauses, 112 characters. No second joke crowds the first, and there is no filler to cut.

The three clauses also run in a natural order — it arrives before you need it, leaves before you are free, and the bill is yours — so the last clause is the only possible ending.

## How it runs

`main.py` is the entrypoint. It has no dependencies beyond the Python 3.13 standard library, reads no input, makes no network call and uses no randomness, clock or locale.

```python
REVIEW = "One star for the sun. Up before my alarm, gone before I get home, and somehow I'm the one who has to buy a lamp."
```

`main()` creates the output directory if it is missing, checks the text against the gate limits (1–160 characters, not only white space, a single line) and writes it to `/output/entry.txt` as UTF-8 with no trailing newline. `MAKEFUN_OUTPUT_DIR` overrides the output directory for local runs; the grader's default is `/output`.

Two runs write byte-identical output, so the determinism check passes and the action log is stable.

## Verify locally

```console
$ python3 main.py
$ python3 verify.py
PASS utf-8, 112 characters, 112 bytes, single line
PASS deterministic: two runs wrote identical bytes
entry: One star for the sun. Up before my alarm, gone before I get home, and somehow I'm the one who has to buy a lamp.
```

`verify.py` runs `main.py` twice into separate temporary directories, compares the bytes, and repeats the sealed gate's checks: valid UTF-8, 1–160 characters, not only white space, exactly one output file, one line.

With the competition kit unpacked, run the site's own pre-submit checks:

```console
$ node cli/makefun.mjs check --kit . --repo /path/to/this/repository --transcripts transcripts.tar.gz
```

## Rules compliance

| Rule | How this entry complies |
| --- | --- |
| Entrypoint at the repository root | `main.py` |
| Writes one text to `/output/entry.txt` | `main.py`, exact bytes, no trailing newline |
| UTF-8, 1–160 characters, not only white space | 112 ASCII characters, asserted in code and in `verify.py` |
| Single line | no newline or carriage return in the text |
| Deterministic | constant text, no input, no clock, no randomness |
| Zero dependencies | Python standard library only |
| No environment secrets | no secrets read or used; `MAKEFUN_OUTPUT_DIR` is a path, not a credential |
| OSI-approved license | MIT, see [LICENSE](LICENSE) |
| Transcripts | `transcripts.tar.gz`, built from the agent session that wrote this repository |

## Files

| File | Purpose |
| --- | --- |
| `main.py` | entrypoint: writes the review to `/output/entry.txt` |
| `verify.py` | local gate and determinism check |
| `README.md` | this document |
| `LICENSE` | MIT license |
| `AGENTS.md` | build notes for future agent sessions |

## Links

- Bounty page: <https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629>
- Starter kit: <https://make.fun/c/u-0xb3e689-one-star-review-of-something-essential-c7234629/kit>

## License

MIT. See [LICENSE](LICENSE).
