# 32 BIT SETUP
##############################
PSSE v34 only supports Python 2.7. 
PSSE software is also only available in 32b. If installing the Python library `psspy` in Anaconda, make sure to use the Anaconda Prompt (not any derivations of this e.g. Anaconda Powershell Prompt) and `set CONDA_FORCE_32BIT=1`. Then create a new environment with `python=2.7` before installing further python packages. 


# TROUBLESHOOTING
##############################
## ImportError: DLL load failed
-------------------------------
The computer loading the `psspy` package from the PSSE folder path that the system is pointing to will look to run a .dll file that should be in the System32 or System64 folders. If it does not exist, follow this blog: https://stackoverflow.com/questions/20201868/importerror-dll-load-failed-the-specified-module-could-not-be-found


# USEFUL LINKS
##############################
- Set up the PSSE folder path: http://www.whit.com.au/blog/2012/10/import-psse-into-your-python-script/
- Useful Python packages to install: http://www.whit.com.au/blog/python-libraries-for-psse-python-training/
