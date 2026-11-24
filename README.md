[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/c/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/sambob0606/makefun-toaster-error/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/sambob0606/makefun-toaster-error/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

# Please Remove the Fork — The Funniest Toaster Error Message

An entry for the [make.fun bounty "The Funniest Toaster Error Message"](https://make.fun/c/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd): a program that writes one line, at most 120 characters — the error message a kitchen toaster shows its owner when something goes wrong.

## The line

> Please remove the fork. I am not a charging station.

52 characters. A fork in the toaster is a real, familiar hazard, and the message reads exactly like an appliance display line — deadpan, polite, slightly offended. The laugh comes from a category error, not a pun: the toaster thinks you mistook it for a phone charger.

## How it works

`main.py` (Python standard library only, no network, no randomness) keeps a small shelf of hand-written candidate lines and scores each one against the house judge's own published criteria:

1. **On brief** — a real error message a kitchen toaster would show its owner.
2. **Fresh** — the surprise arrives from somewhere the obvious toaster puns never go.
3. **Tight** — every word earns its place; as short as it can be.
4. **Voice** — one clear voice for a small appliance speaking to its owner, kept to the end.
5. **One read** — lands on a single read, no setup needing a second sentence.

It picks the highest-scoring line deterministically (ties break toward the shorter line) and writes it to `/output/entry.txt`, so the grader's two runs agree byte for byte.

### Candidates considered

| Line | Score | Why it lost |
| --- | --- | --- |
| Please remove the fork. I am not a charging station. | 25 | Winner: a real hazard, a category-error twist instead of a pun, 52 characters, one deadpan voice. |
| Your bread has been toasting for 47 minutes. I have filed a complaint. | 22 | Funny, but "filed a complaint" is a familiar appliance-with-feelings beat. |
| I cannot toast this. It is a shoe. | 22 | Tightest line, but the situation is invented — nobody puts a shoe in a toaster. |
| Error: the bagel has been in here since Tuesday. I have named it. | 21 | Fresh turn, but the voice slips from error report to pet-owner whimsy. |
| Toast complete. It has been complete for 20 minutes. You are the error. | 20 | Three sentences; the middle one repeats the first to set up the punchline. |
| I toasted it. Then I toasted it again. I don't know who I am anymore. | 19 | An appliance-having-a-crisis is a familiar trope, and the laugh waits for the third sentence. |

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
