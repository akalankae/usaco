#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Last Modified: <date time>
# pylint: disable=invalid-name
# Solution to upload to www.usaco.org
# USACO 2012 November Contest Bronze: Problem 1. Find the Cow!


def cowfind(s) -> int:
    hindLegs = []
    last = -1
    for i in range(len(s)):
        try:
            x = s.index("((", last + 1)
            hindLegs.append(x)
            last = x
        except ValueError:
            break
    foreLegs = []
    last = -1
    for i in range(len(s)):
        try:
            x = s.index("))", last + 1)
            foreLegs.append(x)
            last = x
        except ValueError:
            break
    count = 0
    for x in hindLegs:
        for y in foreLegs:
            if x < y:
                count += 1
    return count


def main():
    """
    Problem solution.
    Reads from `cowfind.in` in current directory and writes to `cowfind.out`
    in current directory
    """

    with open("cowfind.in", "r") as f:
        line = f.read().rstrip()

    with open("cowfind.out", "w") as f:
        f.write(f"{cowfind(line)}\n")


if __name__ == "__main__":
    main()
