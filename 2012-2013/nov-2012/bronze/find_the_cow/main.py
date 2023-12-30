#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Last Modified: <date time>
# pylint: disable=invalid-name

import filecmp
import os

OUTPUT_DIR = "output"


# Get the name of the data directory where where sample input files and
# corresponding sample output files live.
def get_data_dirname(problem_file: str = "problem.txt") -> str:
    """
    Get directory name in which input and output files for testing can be
    found, AKA data directory.
    Input file will have "{number}.in" and output file will have "{number}.out"
    format, where {number} is 1..10
    e.g. 1.in --> 1.out

    """
    data_dirname = ""
    with open(problem_file, "r") as f:
        for line in f:
            if line.startswith("PROBLEM NAME"):
                data_dirname = line.split()[-1]
                break
    return data_dirname


# def cowfind(s) -> list[tuple[int, int]]:
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


# Main function returns the path of output file written to
def main(sample_number: int = 0, problem_file: str = None) -> str:
    """
    Problem solution.
    Reads from `{sample_number}.in` in the data directory and writes to
    `{sample_number}.out` in the output directory
    """
    # If output directory does not exist, make one
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR, 511)

    input_file_name = f"{get_data_dirname()}/{sample_number}.in"
    output_file_name = f"{OUTPUT_DIR}/{sample_number}.out"

    with open(input_file_name, "r") as f:
        line = f.read().rstrip()

    with open(output_file_name, "w") as f:
        f.write(f"{cowfind(line)}\n")

    return output_file_name


# Test Main function
def test_main():
    """
    Tests main.py
    """
    for i in range(1, 11):
        output_file_name = main(i)
        expected_output_file_name = f"{get_data_dirname()}/{i}.out"
        if filecmp.cmp(output_file_name, expected_output_file_name):
            print(f"Test {i} success")
        else:
            print(f"Test {i} failed")


if __name__ == "__main__":
    main()
