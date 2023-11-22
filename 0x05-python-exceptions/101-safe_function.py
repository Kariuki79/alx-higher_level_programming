#!/usr/bin/python3

import sys
from __future__ import print_function

def safe_function(fct, *args):
    try:
        a = fct(*args)
        return a
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
    else:
        return a
