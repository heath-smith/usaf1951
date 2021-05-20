#!user/bin/python
# -*- coding: utf-8 -*-
"""
Helper functions for the AirForceTarget class.
"""

def calc_line_pairs(group, element):
    """
    Calculates line pairs per millimeter for a given group/element combination.

    Params
    -----------
    group (int): group number\n
    element (int): element number\n

    Returns
    -----------
    (float) Line pairs per millimeter.

    """

    lines_per_mm = 2 ** (group + (element - 1) / 6)
    return round(lines_per_mm, 2)

def calc_width(group, element):
    """
    Calculates the width of a single line for a given group/element combination.

    Params
    ----------
    group (int): group number\n
    element (int): element number\n

    Returns
    ----------
    (float) Width of a single line in microns.

    """
    get_pairs_mm = calc_line_pairs(group, element)
    width_um = 1000 / (get_pairs_mm * 2)
    return round(width_um, 2)

def calc_height(group, element):
    """
    Calculates the height of a single line for a given group/element combination.

    Params
    ---------
    group (int): group number\n
    element (int): element number\n

    Returns
    ----------
    (float) Height of a single line in microns.

    """
    
    get_width = calc_width(group, element)
    height_um = 5 * get_width
    return round(height_um, 2)