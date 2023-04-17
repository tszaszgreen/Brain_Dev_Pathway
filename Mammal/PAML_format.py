# Usage take aligment files and format for integration with PAML
# python3 PYcode/PAML_format.py GENE location > FILE.fa

import sys
from Bio import SeqIO

gene = sys.argv[1]
folder = sys.argv[2]

n = 0
for seq_record in SeqIO.parse('%s/%s.nt_ali.fasta' % (folder,gene), "fasta"):
    n = n + 1
    if n < 2:
        print ( " 2", len(seq_record.seq)-3)

for seq_record in SeqIO.parse('%s/%s.nt_ali.fasta' % (folder,gene), "fasta"):
    print(" ")
    #print(seq_record.id)
    id = seq_record.id
    print(id)
    seq = seq_record.seq
    l = len(seq_record.seq)
    end = l - 3
    print(seq[:end])
