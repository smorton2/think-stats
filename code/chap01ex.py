"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file = '2002FemResp.dct',
                dat_file = '2002FemResp.dat.gz'):
    """Creates respondents DataFrame

    dct_file: string file name
    dat_file: string file name

    Returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression = 'gzip', nrows=None)
    # Placeholder for future cleaning function.
    # CleanFemResp(df)
    return df

def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    responses = ReadFemResp()
    response_counts = responses.pregnum.value_counts()

    # Uncomment to print the response counts and validate the assertions.
    # print(response_counts)

    assert(len(responses) == 7643)
    assert(response_counts[0] == 2610)
    assert(response_counts[1] == 1267)
    assert(response_counts[2] == 1432)
    assert(response_counts[3] == 1110)
    assert(response_counts[4] == 611)
    assert(response_counts[5] == 305)
    assert(response_counts[6] == 150)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
