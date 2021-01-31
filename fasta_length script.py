# !/usr/bin/env python3

from Bio import SeqIO
from matplotlib import pyplot as plt
import os
import sys

# Variables

file = (sys.argv[1])


# Functions
def get_length(file):
        lengths = []
        fasta = SeqIO.parse(file, "fasta")
        for records in fasta:
                lengths.append(len(records.seq))
        return (lengths)


def histogram_creation(lengths):
        plt.figure(figsize=(16, 9), facecolor='white')
        plt.xlim([0, max(lengths) + 1])
        plt.xlabel('Read length')
        plt.ylabel('Reads count')
        plt.hist(lengths, bins=5, alpha=0.5, facecolor='blue')
        plt.title("Length distribution in " + os.path.splitext(file)[0],
                  fontsize=14)
        return (plt)


# Main
seqL = get_length(file)
seqL = filter(None, seqL)
seqL = list(map(int, seqL))

hist = histogram_creation(lengths)
hist_file = os.path.abspath(file) + "_distrub_hist.pdf"
hist.savefig(hist_file)
hist.show()
hist.show()