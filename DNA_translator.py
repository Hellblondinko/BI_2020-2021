# !/usr/bin/env python3

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys

file = (sys.argv[1])

with open("Translated_proteins.fasta", 'w') as aa_fa:
    for dna_record in SeqIO.parse(file, 'fasta'):
        # use both fwd and rev sequences
        dna_seqs = [dna_record.seq, dna_record.seq.reverse_complement()]

        # generate all translation frames
        aa_seqs = (s[i:].translate(to_stop=True) for i in range(3) for s in dna_seqs)

        # select the longest one
        max_aa = max(aa_seqs, key=len)

        # write new record
        aa_record = SeqRecord(max_aa, id=dna_record.id, description="translated_sequence")
        SeqIO.write(aa_record, aa_fa, 'fasta')

