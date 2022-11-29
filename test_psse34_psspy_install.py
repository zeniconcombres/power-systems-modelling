import os, sys, glob

# consider adding PSSE_PATH as a system var to avoid path issues
PSSE_PATH = r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
PSSE_PSSPY_PATH = r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY27'
sys.path.append(PSSE_PATH)
sys.path.append(PSSE_PSSPY_PATH)
os.environ['PATH'] += ';' + PSSE_PATH
os.environ['PATH'] += ';' + PSSE_PSSPY_PATH

# will detect a library path mismatch
fns = glob.glob(os.path.join(PSSE_PSSPY_PATH, 'psspy.*'))
if len(fns) == 0:
   print("Who moved my libraries")

import psspy

# if the below executes correctly without fail then PSSE has been installed correctly
psspy.psseinit(100)