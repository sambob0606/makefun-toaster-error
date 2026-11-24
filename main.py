#!/usr/bin/env python3
"""The funniest toaster error message.

Entry for the make.fun bounty "The Funniest Toaster Error Message"
(u-eager-stork-81-9647-the-funniest-toaster-error-436406cd).

The program holds a small shelf of hand-written one-line error messages a
kitchen toaster might show its owner, scores each one against the house
judge's own published criteria, picks the best deterministically, and writes
it to /output/entry.txt.

The judge weighs, most important first:
  1. on_brief  - a real error message a kitchen toaster would show its owner
  2. fresh     - the surprise arrives from somewhere the obvious toaster
                 puns never go (no toast/burnt/crumb wordplay)
  3. tight     - every word earns its place; as short as it can be
  4. voice     - one clear voice for a small appliance speaking to its
                 owner, deadpan or apologetic or quietly dramatic, kept
                 to the end
  5. one_read  - lands on a single read, no setup needing a second sentence

Each criterion is scored 0-5, so 25 is the ceiling. The winner is the
highest total; ties break toward the shorter line, then toward the earlier
candidate, so the grader's two runs agree byte for byte.

Python standard library only. No network, no randomness, no file reads
outside this program: every run writes the same line.
"""

import os

MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"

# Each candidate is one line a real appliance could plausibly display.
# "notes" records, in my own words, why the line earns or loses each point,
# so the scores below are judgements, not magic numbers.
CANDIDATES = [
    {
        "text": "Please remove the fork. I am not a charging station.",
        "scores": {
            # A fork in the toaster is a real, familiar hazard, and the
            # message reads exactly like an appliance display line.
            "on_brief": 5,
            # The surprise is a category error, not a pun: the toaster
            # thinks you mistook it for a phone charger.
            "fresh": 5,
            # 52 characters, two short sentences, nothing to cut.
            "tight": 5,
            # Deadpan throughout; the second sentence keeps the same
            # polite, slightly offended appliance voice.
            "voice": 5,
            # The joke lands the moment the second sentence reframes
            # the first. No setup beyond the fork itself.
            "one_read": 5,
        },
    },
    {
        "text": "Your bread has been toasting for 47 minutes. I have filed a complaint.",
        "scores": {
            # A toaster reporting an over-long cycle is a real error shape.
            "on_brief": 5,
            # The complaint is a fresh turn, but "filed a complaint"
            # is a familiar appliance-with-feelings beat.
            "fresh": 4,
            # 70 characters; "47 minutes" earns its place, but the line
            # needs both sentences to work.
            "tight": 4,
            # Quietly dramatic and consistent: a small machine going
            # through proper channels.
            "voice": 5,
            # One read, though the second sentence does the heavy lifting.
            "one_read": 4,
        },
    },
    {
        "text": "I cannot toast this. It is a shoe.",
        "scores": {
            # A real refusal shape, but nobody puts a shoe in a toaster:
            # the situation itself is invented, not observed.
            "on_brief": 4,
            # Absurd and unexpected, yet the joke is just "wrong object",
            # a single-note surprise.
            "fresh": 4,
            # 34 characters; nothing wasted, the shortest line here.
            "tight": 5,
            # Deadpan and steady, but the voice is flatter than a
            # machine with a grievance.
            "voice": 4,
            # Lands instantly, in one breath.
            "one_read": 5,
        },
    },
    {
        "text": "Error: the bagel has been in here since Tuesday. I have named it.",
        "scores": {
            # A stuck-bagel error is plausible; the "Error:" prefix is
            # exactly how an appliance would say it.
            "on_brief": 5,
            # Naming the bagel is a fresh, odd turn, but it leans on
            # cute rather than on the error itself.
            "fresh": 4,
            # 65 characters; "since Tuesday" is the whole joke's fuel,
            # but "Error:" plus two sentences is a little loose.
            "tight": 4,
            # The voice slips from error report to pet-owner whimsy
            # halfway through.
            "voice": 4,
            # One read, though the second sentence asks for a beat to
            # picture the named bagel.
            "one_read": 4,
        },
    },
    {
        "text": "Toast complete. It has been complete for 20 minutes. You are the error.",
        "scores": {
            # "Toast complete" is a real appliance line; blaming the
            # owner is a believable escalation of it.
            "on_brief": 5,
            # The blame-shift is the fresh move, but "you are the error"
            # is a well-worn tech-joke shape.
            "fresh": 4,
            # 71 characters across three sentences; the middle sentence
            # repeats the first to set up the punchline.
            "tight": 3,
            # Deadpan all the way through, held to the final accusation.
            "voice": 4,
            # Three sentences means three beats; the laugh waits for
            # the last one.
            "one_read": 4,
        },
    },
    {
        "text": "I toasted it. Then I toasted it again. I don't know who I am anymore.",
        "scores": {
            # An over-toasted cycle is a real failure, but the line is
            # really about the machine's feelings, not the error.
            "on_brief": 4,
            # An existential toaster is a fresh angle, though the
            # appliance-having-a-crisis trope is familiar by now.
            "fresh": 4,
            # 69 characters in three sentences; the repetition is the
            # joke, but it costs words.
            "tight": 3,
            # One voice, quietly dramatic from start to finish.
            "voice": 5,
            # The third sentence is the payoff, so the line needs all
            # three beats to land.
            "one_read": 3,
        },
    },
]

CRITERIA = ("on_brief", "fresh", "tight", "voice", "one_read")


def total(candidate):
    """Total score across the judge's five criteria, in order."""
    return sum(candidate["scores"][name] for name in CRITERIA)


def pick(candidates):
    """Highest total wins; ties break toward the shorter line, then the
    earlier candidate, so the choice is stable across runs."""
    best = None
    best_key = None
    for candidate in candidates:
        key = (total(candidate), -len(candidate["text"]))
        if best_key is None or key > best_key:
            best = candidate
            best_key = key
    return best


def main():
    winner = pick(CANDIDATES)
    text = winner["text"]
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            "entry is %d characters, must be 1-%d" % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote %d chars to %s" % (len(text), OUTPUT_PATH))
    print(text)


if __name__ == "__main__":
    main()
