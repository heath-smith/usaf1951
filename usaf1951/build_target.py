#!user/bin/python
# -*- coding: utf-8 -*-
"""
This module is a driver script to build
a USAF1951 resolution target from scratch.

if not installed via pip:
    python -m usaf1951.build_target 3 3 1.5 "soda lime" 5 10 1 7

if installed via pip:
    build_target 3 3 1.5 "soda lime" 5 10 1 7
    (from any directory)
"""

# import external packages
import sys

# import local package modules
from usaf1951.usaf1951 import AirForceTarget

def main():
    """
    Main driver code to be executed on script call.
    """

    # check length of argument list
    if len(sys.argv) == 9:

        # create new instance of AirForceTarget class
        target1 = AirForceTarget(sys.argv[1],
                                sys.argv[2],
                                sys.argv[3],
                                sys.argv[4])

        # iterate over groups 1-3 adding elements
        for g in range(int(sys.argv[5]), int(sys.argv[6])):
            for e in range(int(sys.argv[7]), int(sys.argv[8])):
                target1.add_element(g, e)

        # call extract() to print target info
        # to console
        target1.extract()

    # display error if args > 9
    elif len(sys.argv) > 9:

        sys.stderr.write('Too many parameters.')
        
    # display error if args < 9
    elif len(sys.argv) < 9:

        sys.stderr.write('Not enough parameters.')

if __name__=='__main__':
    main()