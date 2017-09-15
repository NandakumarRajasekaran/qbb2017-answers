Week 1 

1. Run blast and convert the output to fasta format
2. Convert to protein sequences
3. Run mafft and convert back to nucleotide sequences
4. Do some file conversions and have a standard format of one line : one sequences without any sequence id
5. Count number of dN and dS. Ignore any positions where dash is present in query sequence. Calculate Z-score for dN-dS and use -2.326 as a threshold (~99% confidence interval in a one-tailed distribution). 
6. Two options for treating dash in alignment: Count them as no mutation or treat them as non-synonymous mutation. Both options are shown.
