#!/user/bin/env python3
"""
This program resolve a problem of a sideways triangle
The output looks like:

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


def side_tri(l):
    """
    Function print hash signs for l-1 lines
    """
    for row in range(1,l):
        print()

        for hashNum in range(int(5-fabs(4-row)),1,-1):
            print('#',end='')


side_tri(8)


