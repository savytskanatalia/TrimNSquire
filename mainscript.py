# -*- coding: utf-8 -*-

from __future__ import print_function,division

import os
import subprocess
import re

print("Reading in your stupid stuff")

myfiles=os.listdir("/data/raw_data")




print("converting this abomination to a string")
myfav=str(myfiles)



print("finally cleaning the names!")


myfav=re.sub('_1.fastq.gz','',myfav)
myfav=re.sub('_2.fastq.gz','',myfav)
myfav=re.sub('\[','',myfav)
myfav=re.sub('\]','',myfav)
myfav=re.sub('\'','',myfav)
myfav=re.sub('\"','',myfav)

myfavlist=myfav.split(', ')


print("making a proper list to work on!")
mynewlist=[]



for i in range(len(myfavlist)):
    if myfavlist[i] not in mynewlist:
        mynewlist.append(myfavlist[i])

print(mynewlist)

for i in range(len(mynewlist)):
	subprocess.call("skewer -x truseq_adapter_R1.fa -y truseq_adapter_R2.fa -m pe -t 30 raw_data/"+mynewlist[i]+"_1.fastq.gz raw_data/"+mynewlist[i]+"_2.fastq.gz", shell=True)
	subprocess.call("rm raw_data/"+mynewlist[i]+"_*.fastq.gz", shell=True)
	subprocess.call("python Map_ed_f.py -r1 raw_data/"+mynewlist[i]+"_1-trimmed-pair1.fastq -r2 raw_data/"+mynewlist[i]+"_1-trimmed-pair2.fastq -o /data/squire_map_full/ -f /data -r 202 -g /data/hg38_refGene.gtf -v", shell=True)
	subprocess.call("rm raw_data/"+mynewlist[i]+"_1-trimmed-pair*.fastq", shell=True)






