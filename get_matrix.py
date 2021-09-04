import re
import os
import subprocess
import sys

##25
s_dir1 = "/home2/fumigati/aniger_blast_26sps/blast_out/"
##30
s_dir2="/home2/fumigati/aniger_blast_26sps/blast_out3/"

##edit
s_dir = s_dir2
rbh_dir="/home3/bian/A_niger/tables_idcov/"
ni_genes="niger_3993"

genes=[line.rstrip() for line in open(ni_genes)]

s26 = []
os.environ['s_dir'] = str(s_dir)
a = os.popen('ls $s_dir').read().split('\n')
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

print "\t".join(s26)

def get_dict(s1,s2):
	dict={}
	file=rbh_dir+s1+"__"+s2
	f=open(file)
	for line in f:
		line=line.rstrip()
		a=line.split("\t")
		if not a[0] in dict:
			dict[a[0]] = a[1]
	f.close()
	return dict

#for gene in genes:
#gene = "jgi|Aspni_DSM_1|164546|An12g02110m.01_Aspni"
for gene in genes:
	zeile=[]
	for id in s26:
		if id == "Aspni_DSM_1":
			#a=gene.split("|")[3];b=a.split("m")[0]
			zeile.append(gene)
			continue
		#print id
		D = get_dict("Aspni_DSM_1",id)
		a = D[gene]
		#print a
		zeile.append(a.rstrip())
	print "\t".join(zeile)
