#!/user/bin/env python3
"""
This program resolve a problem of a sideways triangle

-- begin out
#
##
###
####
###
##
#
-- end out


ver. 0.1

Grovas - Artur Rozgowski <arczir@gmail.com>

"""
from math import fabs


def side_tri():
    """
    Function print hash signs for 7 lines
    """
    for row in range(1,8):
        print()

        for hashNum in range(int(5-fabs(4-row)),1,-1):
            # range starting sequence with 'fabs()' function
            # reduce necessary reverse counting
            print('#',end='')


