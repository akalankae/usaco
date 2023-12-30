#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Last Modified: <date time>
# pylint: disable=invalid-name


import filecmp

from main import get_data_dirname, main


# testing code goes here
def test_main():
    """
    Tests main.py
    """
    for i in range(1, 11):
        output_file_name = main(i)
        expected_output_file_name = f"{get_data_dirname()}/{i}.out"
        assert filecmp.cmp(output_file_name, expected_output_file_name)
