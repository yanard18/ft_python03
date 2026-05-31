#!/usr/bin/env python3

import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    players = ["Alice", "bob", "Charlie",
               "dylan", "Emma", "Gregory",
               "john", "kevin", "Liam"]

    print(f"Initial list of players: {players}")

    players_cap_all = [p.capitalize() for p in players]
    print(f"New list with all names capitaliz {players_cap_all}")

    players_cap_only = [p for p in players if p[0].isupper()]
    print(f"New list of capitalized names only: {players_cap_only}\n")

    score_dict = {p: random.randint(100, 999) for p in players_cap_all}
    print(f"Score dict: {score_dict}")

    avg = sum(score_dict.values()) / len(score_dict.keys())
    print(f"Avarage score {round(avg, 2)}")

    score_over_avg = {p: s for (p, s) in score_dict.items() if s > avg}
    print(f"High scores: {score_over_avg}")
