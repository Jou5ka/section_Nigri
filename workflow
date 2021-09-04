##blast results -> RBH pairs
tables.py -> tables_idcov/

##find orthologs
complete.py -> niger_3993

##table
get_matrix.py >30_3993; vi add "#"

#get seq
seq.py -> seq_set_30

##alignment etc.
mafft.sh; gblocks.sh
ls seq_set_30/*-gb | wc -l 
! use seq_len.py to check the result from Gblocks! orz
seqName2Long.py

##concatenate seq
concatenate.py -> concat_30.fa

##phylogenetic analysis
raxml_prot.sh -> *.out

