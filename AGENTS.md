# Build notes

Repository for the make.fun bounty `u-0xb3e689-one-star-review-of-something-essential-c7234629`.

## What the grader does

- Runs `main.py` in a sandbox with no network and a 60 s wall budget, twice, and compares the outputs manifest byte for byte.
- Reads `/output/entry.txt` as the entry. The gate requires valid UTF-8, 1 to 160 characters, not only white space. The judge then compares the text with other entries two at a time.

## Commands

```console
# write the entry to /output/entry.txt (or MAKEFUN_OUTPUT_DIR)
python3 main.py

# gate checks and determinism, both runs compared byte for byte
python3 verify.py

# the site's own pre-submit checks, from the unpacked kit
node cli/makefun.mjs check --kit . --repo <this repository> --transcripts transcripts.tar.gz

# rebuild the transcripts bundle from the agent session that built this repository
node cli/makefun.mjs bundle --repo <this repository> --openhands-dir /var/openhands/conversations \
  --harness openhands --harness-version 1.63.1 --provider deepseek \
  --model openhands/deepseek-v4.1-flash --effort default --out transcripts.tar.gz
```

## Conventions

- Keep the review one line and under 160 characters; `verify.py` enforces it.
- Keep the entry text a single module constant so the output stays deterministic.
- Standard library only. No network, no clock, no randomness, no secrets.
- ASCII only, so the byte count and the character count agree.
