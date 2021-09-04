# -*- coding: utf-8 -*-
import sys
import re
import os

#dir="/home3/bian/Aniger/blastp_out/"
dir = "/home2/fumigati/aniger_blast_26sps/blast_out/"
dir2 = "/home2/fumigati/aniger_blast_26sps/blast_out2/"
dir3 = "/home2/fumigati/aniger_blast_26sps/blast_out3/"

out_dir = "tables_idcov/"

s26 = []
os.environ['dir3'] = str(dir3)
a = os.popen('ls $dir3').read().split('\n')
for i in a:
	b = re.split('_to_|.out',i)
	try:
		for j in [b[0],b[1]]:
			if not j in s26:
				s26.append(j)
	except IndexError:
		pass
s26.remove("Aspni_DSM_1");s26.insert(0,"Aspni_DSM_1")
#s26.remove("Aspergillus_niger_IFM51935")
num = len(s26)	#30

def getTophit(sp1,sp2):
	cov = 0.6
	ident = 60
	pLen = 300
	if os.path.isfile(dir+sp1+"_to_"+sp2+".out"):
		f1=dir+sp1+"_to_"+sp2+".out"
		f2=dir+sp2+"_to_"+sp1+".out"	
	elif os.path.isfile(dir2+sp1+"_to_"+sp2+".out"):
		f1=dir2+sp1+"_to_"+sp2+".out"
                f2=dir2+sp2+"_to_"+sp1+".out"	
	else:
		f1=dir3+sp1+"_to_"+sp2+".out"
                f2=dir3+sp2+"_to_"+sp1+".out" 
	dict1={}
	f=open(f1)
	for line in f:
		tmp = line.split("\t")
		qry = tmp[0]
		subj = tmp[1]
		
		qlen = float(tmp[2])
		length = float(tmp[4])
		
		if qry in dict1:
			continue
		#if float(tmp[6]) >= ident:      #out: tables_ident
		#if length >= qlen*cov:
		if float(tmp[6]) >= ident and length >= qlen*cov:       #out: tables_idcov
		#if float(tmp[6]) >= ident and length >= qlen*cov and int(tmp[2]) >= pLen :
			dict1[qry] = subj
	f.close()
	
	dict2={}
	f=open(f2)
	for line in f:
		tmp = line.split("\t")
                qry = tmp[0]
                subj = tmp[1]

                qlen = float(tmp[2])
                length = float(tmp[4])
		
		if qry in dict2:
			continue
                #if float(tmp[6]) >= ident:	#out: tables_ident
		#if length >= qlen*cov:
		if float(tmp[6]) >= ident and length >= qlen*cov:
		#if float(tmp[6]) >= ident and length >= qlen*cov and int(tmp[2]) >= pLen :
			dict2[qry] = subj
	f.close()

	##pick the share pairs
	share = {}
	for id1 in dict1:
		value = dict1[id1]
		if value in dict2:
			if id1 == dict2[value]:
				share[id1] = value
	return share

#getTophit(s26[0],s26[0])

def main():
	i=0
	for s1 in s26:
		for idx in range(i,num):
			s2=s26[idx]
			if os.path.isfile(out_dir+s1+"__"+s2):
				continue

			tophit=getTophit(s1,s2)
	
			f=open(out_dir+s1+"__"+s2,"a")
			for key in tophit:
				f.write(key+"_"+s1+"\t"+tophit[key]+"_"+s2+"\n")
			f.close()
		i+=1	
if __name__ == "__main__":
    main()
