#!/usr/bin/env python3

import random


"""
Note (Oct. 2020): as of v3.9, Python has officially deprecated
random.sample() working on sets, with the official guidance being to
explicitly convert the set to a list or tuple before passing it in,
though this doesn't solve the efficiency problems.

>>> random.sample(set('abcdefghijklmnopqrstuvwxyz'), 1) ['f']

Documentation:
https://docs.python.org/3/library/random.html#random.sample

Note that choosing random elements from a set is extremely inefficient
no matter how you do it - it takes time proportional to the size of
the set, or worse if the set's underlying hash table is sparse due to
removed elements.

Instead, you should probably use a different data structure that
supports this operation efficiently.

Reference:
https://stackoverflow.com/questions/15837729/random-choice-from-set
"""

ACHIEVEMENTS_POOL = ('Crafting Genius', 'Strategist', 'World Savior',
                     'Speed Runner', 'Survivor', 'Master Explorer',
                     'Treasure Hunter', 'Unstoppable', 'First Steps',
                     'Collector Supreme', 'Untouchable', 'Sharp Mind',
                     'Boss Slayer')


def gen_players(names: tuple[str, ...]) -> tuple[tuple[str, set[str]], ...]:
    return tuple((name, gen_player_achievements()) for name in names)


def gen_player_achievements() -> set[str]:
    rnd_achievements = random.sample(
        ACHIEVEMENTS_POOL,
        k=random.randint(1, len(ACHIEVEMENTS_POOL))
    )

    return set(rnd_achievements)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    players = gen_players(("Alice", "Bob", "Charlie", "Dylan"))

    all_achvmnt_sets = [achv for name, achv in players]
    all_achvmnts = set.union(*all_achvmnt_sets)

    for name, achv in players:
        print(f"Player {name}: {achv}")

    print(f"\nAll distinct achievements: {all_achvmnts}")

    common_achvmnts = set.intersection(*all_achvmnt_sets)
    print(f"\nCommon achievements: {common_achvmnts}\n")

    for name, achv in players:
        other_achvmnt_sets = [s for s in all_achvmnt_sets if s is not achv]
        only_achv = achv.difference(*other_achvmnt_sets)
        print(f"Only {name} has: {only_achv}")

    print()
    for name, achv in players:
        print(f"{name} is missing: {all_achvmnts - achv}")
