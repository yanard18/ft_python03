#!/usr/bin/env python3

import math


def try_float(x: str) -> float:
    try:
        return float(x)
    except ValueError as e:
        raise ValueError(f"Error on parameter '{x}': {e}")


def distance(p1: tuple[float, float, float],
             p2: tuple[float, float, float]) -> float:
    return math.sqrt(
        (p2[0] - p1[0])**2 +
        (p2[1] - p1[1])**2 +
        (p2[2] - p1[2])**2
    )


def get_pos_input() -> tuple[float, float, float]:
    user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
    args = user_input.replace(" ", "").split(",")

    if (len(args) != 3):
        raise Exception("Invalid syntax")

    return (
        try_float(args[0]),
        try_float(args[1]),
        try_float(args[2])
    )


def get_pos() -> tuple[float, float, float]:
    while True:
        try:
            pos = get_pos_input()
            print(f"Got a first tuple: {pos}")
            print(f"It includes: X={pos[0]} Y={pos[1]} Z={pos[2]}")
            return pos
        except Exception as e:
            print(f"{e}")


def get_player_pos() -> None:
    print("Got a first set of coordinates")
    p1 = get_pos()

    print(f"Distance to center: {round(distance(p1, (0, 0, 0)), 4)}\n")

    print("Got a second set of coordinates")
    p2 = get_pos()

    print("Distance between the 2 sets of coordinates: " +
          f"{round(distance(p1, p2), 4)}\n")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    get_player_pos()
