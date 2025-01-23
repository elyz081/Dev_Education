#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script Description:
-------------------
[Provide a brief description of the functionality of the script.]

Features:
---------
- [Feature 1]
- [Feature 2]
- [Feature 3]

Usage:
------
Example of running the script:
    [Provide example command-line usage.]

Parameters:
-----------
[Provide details of each parameter and its purpose.]

---------------------------------------------------------------
Reference:
[1] 
---------------------------------------------------------------
"""
#Remember to organize your imports in alaphabetic order

#Python Built-in Utilities
import argparse
import logging

#External Dependencies
import numpy as np
import nibabel as nib

#Scilpy Modules
from scilpy.io.utils import (assert_inputs_exist, add_verbose_arg)
from scilpy.version import version_string

def _build_arg_parser():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawTextHelpFormatter,
                                epilog=version_string)
                                
    # Add arguments here 
    p.add_argument('required_argument', help='Small description of the required argument')
    p.add_argument('--optional_argument', type=str, help='Small description of the optional argument')
    
    add_verbose_arg(p)
    
    return p

def main():
    parser = _build_arg_parser()
    args = parser.parse_args()
    logging.getLogger().setLevel(logging.getLevelName(args.verbose))
    
    #HAVE FUN :)

if __name__ == "__main__":
    main()
