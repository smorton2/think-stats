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

def ValidatePregnum(responses):

    # Read pregnancy data and create a dictionary with the mapped values.
    preg_data = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg_data)

    # Set key for responses and preg_map
    #
    for index, pregnum in responses.pregnum.iteritems():
        caseid = responses.caseid[index]
        indices = preg_map[caseid]


        if len(indices) != pregnum:
            print(caseid)
            return False
            
    return True

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
    assert(ValidatePregnum(responses))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
