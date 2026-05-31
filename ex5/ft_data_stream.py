#!/usr/bin/env python3

import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str]]:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep",
               "grab", "move", "climb",
               "swim", "release"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)

        yield (player, action)


def consume_event(lst: list[tuple[str, str]]) -> Generator[tuple[str, str]]:
    while len(lst) > 0:
        i = random.randint(0, len(lst) - 1)
        yield lst.pop(i)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    event_gen = gen_event()

    for i in range(1000):
        player, action = next(event_gen)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events = []
    for i in range(10):
        ten_events.append(next(event_gen))

    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")
