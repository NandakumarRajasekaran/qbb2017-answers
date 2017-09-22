
velvet gives poor assembly compared to spades.

For high coverage reads, spades gives only 1 contig. 

For producing dotplot, I have not accounted for +/- strand
but still the plots look OK. The contigs are not perfectly aligned with each other
i.e. If contig i starts at 1000 and ends at 2000, contig i+1 may start at 1950 instead 
of 2001. This may have to do with +/- strands. 

canu assembler takes a few minutes to run but gives better alignment

low and high refer to coverage