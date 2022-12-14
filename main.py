"""
Author: Inez Zheng @zeniconcombres
Date Created: 2022-11-14

Script created to run PSSE studies and generate 
basic scripts that can be used with the PSSE Xplore34 
free version of the software.
"""

import os, sys, glob
import matplotlib
import numpy as np
import pandas as pd
from pandas import DataFrame as df

# consider adding PSSE_PATH as a system var to avoid path issues
PSSE_PATH = r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
PSSE_PSSPY_PATH = r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY27'
sys.path.append(PSSE_PATH)
sys.path.append(PSSE_PSSPY_PATH)
os.environ['PATH'] += ';' + PSSE_PATH
os.environ['PATH'] += ';' + PSSE_PSSPY_PATH

fns = glob.glob(os.path.join(PSSE_PSSPY_PATH, 'psspy.*'))
if len(fns) == 0:
   print("Who moved my libraries")

import psspy

psspy.psseinit(100)
