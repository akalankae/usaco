#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Last Modified: <date time>
# pylint: disable=invalid-name
# Input data files and corresponding expected output files will live inside a
# directory by the name of the problem.  Output files written by the user's
# main() function will live inside `OUTPUT_DIR`.  File names will be N.in for
# input files and N.out for output files, where N = 1..10

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


# Main function returns the path of output file written to
def main(sample_number: int = 0, problem_file: str = None) -> str:
    """
    Problem solution.
    Reads from `{sample_number}.in` in the data directory and writes to
    `{sample_number}.out` in the output directory
    """
    # If output directory does not exist, make one
    if not os.path.exists(OUTPUT_DIR) or os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR, 511)

    data_dir = get_data_dirname()
    input_file_name = f"{data_dir}/{sample_number}.in"
    output_file_name = f"output/{sample_number}.out"

    return output_file_name


# Test Main function
def test_main():
    """
    Tests main.py
    """
    data_dir = get_data_dirname()
    for i in range(1, 11):
        output_file_name = main(i)
        expected_output_file_name = f"{data_dir}/{i}.out"
        if filecmp.cmp(output_file_name, expected_output_file_name):
            print(f"Test {i} success")
        else:
            print(f"Test {i} failed")


if __name__ == "__main__":
    main()
