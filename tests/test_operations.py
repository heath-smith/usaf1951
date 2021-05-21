#!user/bin/python
# -*- coding: utf-8 -*-
"""
Test module for testing the helper functions
of the AirForceTarget package.
"""

# import external packages
import numpy as np
import unittest
from pathlib import Path
import sys
import os

# import package files
from usaf1951.operations import calc_height, calc_line_pairs, calc_width

# test the get_moe_data method
class TestOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # define the test variables
        cls.test_g = 7
        cls.test_e = 6
        cls.test_lp = 228.07
        cls.test_width = 2.19
        cls.test_height = 10.95

    def test_calc_line_pairs(self):
        """
        Test the calc_line_pairs() function.
        """
        # call calc_line_pairs
        test_lp = calc_line_pairs(self.test_g, self.test_e)

        # assert values are equal
        self.assertEqual(test_lp, self.test_lp)

    def test_calc_width(self):
        """
        Test the calc_width() function.
        """
        # call calc width
        test_width = calc_width(self.test_g, self.test_e)

        # assert values are equal
        self.assertEqual(test_width, self.test_width)

    def test_calc_height(self):
        """
        Test the calc_height() function.
        """
        
        # call calc_height function
        test_height = calc_height(self.test_g, self.test_e)

        # assert equality
        self.assertEqual(test_height, self.test_height)


if __name__=='__main__':
    unittest.main()