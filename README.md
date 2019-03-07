# TrimNSquire
Trim your fastqs and SQuIRE them up! 

This Dockerfile sets a container up to trim the reads with Skewer ( https://github.com/relipmoc/skewer ) and quantify retrotransposons&/genes with SQuIRE ( https://github.com/wyang17/SQuIRE ).

As of now, it is being tested on SQuIRE Map. 
Allows to list the sample names from paired-end reads, trim them for adapters, pass on to SQuIRE mapping function.

WARNING: cleans up both trimmed and untrimmed fastqs to save up space!


##UPDATE/DOWNLOAD SIX MODULE
pip install six
