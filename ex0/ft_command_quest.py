#!/usr/bin/env python3

import sys


def print_args() -> None:
    print(f"Program name: {sys.argv[0]}")

    user_args = sys.argv[1:]

    if not user_args:
        print("No arguments provided!")
        return

    print(f"Arguments received: {len(user_args)}")

    i = 1
    for arg in user_args:
        print(f"Argument {i}: {arg}")
        i += 1

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    print_args()
