#!/usr/bin/env python3


import argparse

# create an ArgumentParser object ('parser') that will hold all the information necessary to parse the command line
parser = argparse.ArgumentParser(description = "generates a parse script for FSA and GFF files")

# add positional arguments, i.e. the required input, so whatever I put after the write_trestles_PBS.py will become the job name
parser.add_argument("fsa_file", help= "The name of the FSA file" )
parser.add_argument("gff_file", help= "The name of the GFF file" )


# parse the command line arguments
args = parser.parse_args()

# creating args for the file names
fsa_file = args.fsa_file
gff_file = args.gff_file

# Opening and storing FASTA file as a list, fastalines = genome of qatermelon
with open("watermelon.fsa") as w:
    fastalines = w.read().splitlines()
    
# open the GFF file #
gff_file = "watermelon.gff"
gff = open(gff_file, "r")

# reopen the fasta file since it closed eariler in the with loop
fsa_file = "watermelon.fsa"
fsa = open(fsa_file, "r")

# defining the function to base the for loop on 
# calculate the GC content for this feature
def get_gc_content(substring):
    length = len(substring)
    G_count = substring.count('G')
    C_count = substring.count('C')
    GC_content = (G_count + C_count) / length
    return GC_content

# parse the files and extract the genome features 

#startandstops = []

for line in gff:
    line = line.rstrip('\n')
    fields = line.split('\t')
    start = (int(fields[3]) - 1)
    stop = (int(fields[4]) - 1)
    output = fastalines[start:stop]
    #startsandstops.append(output)
    print(get_gc_content(output))
    
gff.close()