# -*- coding: utf-8 -*-
import sys
import re
import os

#dir="/home2/fumigati/aniger_blast_26sps/blast_out/"
dir="/home2/fumigati/aniger_blast_26sps/blast_out3/"
s26 = []
os.environ['dir'] = str(dir)
a = os.popen('ls $dir').read().split('\n')
for i in a:
        b = re.split('_to_|.out',i)
        try:
                for j in [b[0],b[1]]:
                        if not j in s26:
                                s26.append(j)
        except IndexError:
                pass
s26.remove("Aspni_DSM_1");s26.insert(0,"Aspni_DSM_1")

##remove IFM51935
#s26.remove("Aspergillus_niger_IFM51935")

num = len(s26)

dir = "tables_idcov/"
##s1_s2
def tophit(s1,s2):
	D={}
	f=open(dir+s1+"__"+s2)
	for line in f:
		line=line.rstrip()
		a=line.split("\t")
		D[a[0]] = a[1]
	f.close()
	return D

D1=tophit(s26[0],s26[1])

q=0
for nig in D1:
	#print nig,D1[nig]
	
	q+=1
	flag=False
	i = 0
	for idx in range(i,num):
		s1 = s26[idx]
		D2 = tophit("Aspni_DSM_1",s1)
		## nig in s1 exist in si
		if not nig in D2:
			flag = True
			i+=1
			continue
 	
		gene = D2[nig]
		
		## in s1,si
		j=i+1
		while j < num:						
			s2 = s26[j]
			#print i,j,s1,s2
			D3 = tophit(s1,s2)
			if not gene in D3:
				flag = True
				break
			j+=1
		i+=1
		
	#break
	if flag == False:
		print nig

