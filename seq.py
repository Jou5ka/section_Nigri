# -*- coding: utf-8 -*-
import os
import re
from Bio import SeqIO
import pandas as pd

##edit
a=open("30_3993").read().splitlines()
out="seq_set_30/"

ids=a[0].split("\t")
ids.remove("#Aspni_DSM_1");ids.insert(0,"Aspni_DSM_1")

def get_aaseq(strain):
	for file in os.listdir("/home2/fumigati/aniger_blast_26sps/protein_fasta_30strains"):
		if strain in file:
			return "/home2/fumigati/aniger_blast_26sps/protein_fasta_30strains/"+file


k=0
for line in a:
	if "#Aspni" in line:
		continue
	line=line.rstrip()
	genes26=line.split('\t')
	if os.path.isfile(out+genes26[0]+".fa"):
		continue
	j=-1
	file=out+genes26[0]+".fa"
	f=open(file,"a")
	for gene in genes26:
		j+=1
		strain=ids[j]
		g = get_aaseq(strain)
		
		for rec in SeqIO.parse(g,"fasta"):
			id1 = rec.id
			idd = id1 + "_" + strain
			if idd == gene:
				f.write("\n>"+gene+"\n")
				f.write(str(rec.seq))
				continue
		
	f.close()

