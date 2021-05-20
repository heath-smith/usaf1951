#!user/bin/python
# -*- coding: utf-8 -*-
"""
Test module for testing and asserting methods inside
the AirForceTarget class.
"""

# import external packages
import numpy as np
import unittest
from pathlib import Path
import sys
import os

# import package files
from usaf1951.usaf1951 import AirForceTarget

# test the get_moe_data method
class TestAirForceTarget(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Setup the test class and initialize test variables.
        """
        # define test variables
        cls.test_elements = dict({(5, 5):[50.80, 9.84, 49.20]})  # test dict
        cls.test_h = 3  # test height
        cls.test_w = 3  # test width
        cls.test_th = 1.5  # test thickness
        cls.test_mat = 'soda lime'  # test material
        cls.test_g = 5  # test group
        cls.test_e = 5  # test element

        # create a dict with multiple elements
        # ONLY TO BE USED IN TEST_GET_CD METHOD !!!!!!
        cls.test_elements_2 = dict({(5, 5):[50.80, 9.84, 49.20],
                                    (3, 3):[10.08, 49.61, 248.03],
                                    (4, 4):[22.63, 22.10, 110.50],
                                    (7, 6):[228.07, 2.19, 10.96]})
        # define test cd value, only for test_get_cd method
        cls.expected_cd = 2.19

    def test_init(self):
        """
        Test the __init__ method of the AirForceTarget class.
        """

        # create instance of AirForceTarget w/ params
        test_targ = AirForceTarget(self.test_h,
                                    self.test_w,
                                    self.test_th,
                                    self.test_mat)
        
        # assert class members are equal to input variables
        self.assertEqual(test_targ.height, self.test_h)
        self.assertEqual(test_targ.width, self.test_w)
        self.assertEqual(test_targ.thickness, self.test_th)
        self.assertEqual(test_targ.material, self.test_mat)

    def test_add_element(self):
        """
        Test the add_element() method of the AirForceTarget class.
        """

        # create instance of AirForceTarget w/ params
        test_targ = AirForceTarget(self.test_h,
                                    self.test_w,
                                    self.test_th,
                                    self.test_mat)

        # call add_element method
        test_targ.add_element(self.test_g, self.test_e)

        # assert 'elements' class member is equal to test
        self.assertEqual(test_targ.elements, self.test_elements)

    def test_remove_element(self):
        """
        Test the remove_element() method of the AirForceTarget class.
        """

        # create instance of AirForceTarget w/ params
        test_targ = AirForceTarget(self.test_h,
                                    self.test_w,
                                    self.test_th,
                                    self.test_mat)

        # call add_element method
        test_targ.add_element(self.test_g, self.test_e)

        # call remove_element method
        test_targ.remove_element(self.test_g, self.test_e)

        # assert 'elements' class member is empty
        self.assertEqual(0, len(test_targ.elements))

    def test_get_cd(self):
        """
        Test the get_cd() method of the AirForceTarget class.
        """

        # create instance of AirForceTarget w/ params
        test_targ = AirForceTarget(self.test_h,
                                    self.test_w,
                                    self.test_th,
                                    self.test_mat)

        # shortcut to override 'elements' class member 
        # only to be used within this test method
        test_targ.elements = self.test_elements_2

        test_cd = test_targ.get_cd()

        # assert 'elements' class member is empty
        self.assertEqual(test_cd, self.expected_cd)

    def test_extract(self):
        """
        Test the extract() method of the AirForceTarget class.
        """

        # create instance of AirForceTarget w/ params
        test_targ = AirForceTarget(self.test_h,
                                    self.test_w,
                                    self.test_th,
                                    self.test_mat)

        # shortcut to override 'elements' class member 
        # only to be used within this test method
        test_targ.elements = self.test_elements_2

        # call extract method
        test_targ.extract()

    #@classmethod
    #def tearDownClass(cls):
    #    """
    #    Tear down test class if needed.   
    #    """
    #    del cls.layers
    #    del cls.materials


if __name__=='__main__':
    unittest.main()