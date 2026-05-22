#!/usr/bin/env python3

import sys


def try_int(x: str) -> int | None:
    try:
        return int(x)
    except ValueError:
        print(f"Invalid parameter: '{x}'")
        return None


if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    script_name = sys.argv[0]
    args = sys.argv[1:]

    scores = [s for s in [try_int(x) for x in args] if s is not None]

    if not scores:
        print("No scores provided."
              f" Usage: python3 {script_name} <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
