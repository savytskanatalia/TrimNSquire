# TrimNSquire
Trim your fastqs and SQuIRE them up! 

This Dockerfile sets a container up to trim the reads with Skewer ( https://github.com/relipmoc/skewer ) and quantify retrotransposons&/genes with SQuIRE ( https://github.com/wyang17/SQuIRE ).

It allows you trimming your fastqs, aligning and quantifying them in one container:)
The script requeires one argument to run - the number of threads.
To run it:
python mainscript.py $N-of-threads$

This script, as well as the SQuIRE scripts, are written in python 2.7.


WARNING: cleans up both trimmed and untrimmed fastqs to save up space!


##UPDATE/DOWNLOAD SIX MODULE
pip install six
