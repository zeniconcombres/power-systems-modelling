import os, sys
import matplotlib
import numpy as np
import pandas as pd
from pandas import DataFrame as df

# consider adding PSSE_PATH as a system var to avoid path issues
PSSE_PATH = r'C:\Program Files (x86)\PTI\PSSEXplore34'
PSSE_PSSPY_PATH = r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY27'
sys.path.append(PSSE_PATH)
sys.path.append(PSSE_PSSPY_PATH)
os.environ['PATH'] += ';' + PSSE_PATH
os.environ['PATH'] += ';' + PSSE_PSSPY_PATH

import psspy

psspy.psseinit(100)
