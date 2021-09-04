# -*- coding: utf-8 -*-
import os
import re
from Bio import SeqIO

##edit
sset="seq_set_nucl/"
f=open('30_3993')
end = "-gb"
end = "mafft"

line=f.readline()
a=line.split("\t")

strains=[]
for i in a:
	if "#" in i:
		i=i.split("#")[1]
	strains.append(i.rstrip())

#print strains
#"""
i=0
for item in strains: 
	print ">"+item          
 	tmp = ""
	for filename in os.listdir(sset):
		if filename.endswith(end):
			path=sset + filename		
			j=0
			for record in SeqIO.parse(path,"fasta"):
				if j==i:
					tmp+=record.seq		
				j+=1
	
			
	i+=1
	print tmp
f.close()	
#"""
