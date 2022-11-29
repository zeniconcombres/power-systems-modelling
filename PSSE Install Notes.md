# DOWNLOAD
Go to Siemens website and request for the free version of PSSE. This will provide you with an .exe download. 
Run download and install all the associated Python and compiler / support packages (basically just click through everything saying yes).


# 32 BIT SETUP
PSSE v34 only supports Python 2.7. 
PSSE software is also only available in 32b. If installing the Python library `psspy` in Anaconda, make sure to use the Anaconda Prompt (not any derivations of this e.g. Anaconda Powershell Prompt) and `set CONDA_FORCE_32BIT=1`. Then create a new environment with `python=2.7` before installing further python packages.
`>> conda create -n "py2_32b" python=2.7`


# TROUBLESHOOTING
Run test_psse34_psspy_install.py to check basic install is correct and have PSSE open on your computer (this is very important!) before running the script.

Successful test of installation should output something similat to the following in the terminal:
     PSS(R)E Version 34
     Copyright (c) 1976-2022
     Siemens Industry, Inc.,
     Power Technologies International                            (PTI)
     This program is a confidential  unpublished  work  created  and  first
     licensed in 1976.  It is a trade secret which is the property of  PTI.
     All use,  disclosure,  and/or reproduction not specifically authorized
     by  PTI  is prohibited.   This  program is protected  under  copyright
     laws  of  non-U.S.  countries  and  by  application  of  international
     treaties.  All  Rights  Reserved  Under  The  Copyright  Laws.


               SIEMENS POWER TECHNOLOGIES INTERNATIONAL

            50 BUS POWER SYSTEM SIMULATOR--PSS(R)E-34.3.2

                 INITIATED ON TUE, NOV 29 2022  13:23

## ImportError: DLL load failed
The computer loading the `psspy` package from the PSSE folder path that the system is pointing to will look to run a .dll file that should be in the System32 or System64 folders. If it does not exist, follow this blog: https://stackoverflow.com/questions/20201868/importerror-dll-load-failed-the-specified-module-could-not-be-found

Other DLL fail blog pages:
- https://psspy.org/psse-help-forum/question/2751/importerror-dll-load-failed/
- https://psspy.org/psse-help-forum/question/7551/python-37-w-psse-34/


# USEFUL LINKS
- Set up the PSSE folder path: http://www.whit.com.au/blog/2012/10/import-psse-into-your-python-script/
- Useful Python packages to install: http://www.whit.com.au/blog/python-libraries-for-psse-python-training/
