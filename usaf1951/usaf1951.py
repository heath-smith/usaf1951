#""" usaf1951
#
#This module contains the class AirForceTarget which allows users to design
#and edit a custom USAF 1951 resolution target.
#
#Examples
#------------
#To install locally, download the package
#and run 'python -m pip install <path to package>'
#
#"""


# import dependencies
import os
import sys
import pandas as pd

# import operations file
from .operations import calc_height, calc_line_pairs, calc_width

# class declaration AirForceTarget
class AirForceTarget:
    """
    AirForceTarget class allows users to add custom elements to a USAF 1951
    test target design. Also allows users to specify dimensions and materials.

    Params
    ---------
    h (int): height of target in inches\n
    w (int): width of target in inches\n
    t (float): thickness of target in millimeters\n
    mat (str): substrate material

    Examples
    ---------
    new_target = AirForceTarget(3, 3, 1.5, 'soda lime')\n
    new_target.add_element(5, 5)\n
    new_target.remove_element(5, 5)\n
    cd_val = new_target.get_cd()\n

    Use the extract method to write all target info to output stream.
    """

    def __init__(self, h, w, t, mat):
        """
        Initializes the AirForceTarget class by defining class members using
        input parameters.

        Params
        ---------
        h (int): height of target in inches\n
        w (int): width of target in inches\n
        t (float): thickness of target in millimeters\n
        mat (str): substrate material

        Returns
        ---------
        Does not return any values.
        """
        # set class member variables
        self.elements = dict({})  # elements : dictionary { (g, e) : [lp/mm, width, height] }
        self.height = int(h)
        self.width = int(w)
        self.thickness = float(t)
        self.material = str(mat)

    def add_element(self, group, element):
        """
        Adds an element to the target design and calculates lp/mm, width, & height.

        Params
        ---------
        group (int): target group number\n
        element (int): target element number\n

        Does not return any values.
        """

        # use lp/mm operation
        lines_per_mm = calc_line_pairs(group, element)

        # use width operation
        line_width = calc_width(group, element)

        # use height operation
        line_height = calc_height(group, element)

        # combine line info into list
        elementInfo = [lines_per_mm, line_width, line_height]


        try:
            # try to add item to 'elements' class member
            self.elements[(group, element)] = elementInfo

        except KeyError:

            # handle KeyError exception
            sys.stderr.write(f'Error adding element {element} to group {group}.\n')

    def remove_element(self, group, element):
        """
        Removes an element from the target. 

        Params
        ---------
        group (int): group number of element to be removed\n
        element (int): element to be removed\n

        Returns
        ---------
        Does not return any values.

        Raises
        ---------
        Raises KeyError exception if group, element combination not found.\n
        """

        try:
            # attempt to delete key-value pair
            del self.elements[(group, element)]

        except KeyError:
            # handle KeyError exception
            sys.stderr.write(f'Error removing element {element} to group {group}.\n')

    def get_cd(self):
        """
        Finds the smallest line width of the target, called the 'critical dimension'.

        Params
        ---------
        Does not accept any input parameters.

        Returns
        ---------
        (float) The value of the critical dimension. Writes error to output stream
        and returns 0.0 if the target does not contain any elements.
        """

        # check if 'elements' contains values
        if self.elements:

            # get the first available element and cd value
            first_index = next(iter(self.elements))
            cd_val = self.elements[first_index][1]

            # iterate through 'elements' dictionary
            for key in self.elements:

                # compare current cd to cd_val
                if self.elements[key][1] < cd_val:

                    # reset cd_val if conditition is true
                    cd_val = self.elements[key][1]

        else:

            # if empty, output error message
            sys.stderr.write('Please add an element to the target design.\n')

            # return a null cd
            cd_val = 0.0


        return  cd_val

    def extract(self):
        """
        Writes all target information to output stream.

        Params
        ---------
        Does not accept any input parameters.

        Returns
        ---------
        Does not return any values. Writes 'No elements found.' if target is empty.

        """

        # write the target class members first
        sys.stdout.write('Target Specs\n---------------\n')
        sys.stdout.write('Height: ' + str(self.height) + ' in\n'
                        + 'Width: ' + str(self.width) + ' in\n'
                        + 'Material: ' + str(self.material) + '\n')

        # check if 'elements' contains any values
        if self.elements:

            # create a dataframe with dictionary
            col_names = ['lp/mm', 'width(um)', 'height(um)']
            target_df = pd.DataFrame.from_dict(self.elements, orient='index', columns=col_names)
            sys.stdout.write('\nElements\n---------------\n' + str(target_df) + '\n')

            # call get_cd and write to output stream
            sys.stdout.write('\nThe critical dimension is ' + str(self.get_cd()) + ' microns.\n')

        else:

            # write error message to console
            sys.stderr.write('No elements found.')
