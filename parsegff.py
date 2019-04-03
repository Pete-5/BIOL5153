#! /usr/bin/python

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

startsandstops = []

for line in gff:
    line = line.rstrip('\n')
    fields = line.split('\t')
    start = int(fields[3]) - 1
    stop = int(fields[4]) - 1
    output = fastalines[start:stop]
    startsandstops.append(output)
    print(get_gc_content(output))
    
gff.close()