I used snpEff R64-1-1.86 database

Consequences of high highest quality variants:

I sorted the ann.vcf file by QUAL column and looked at the five highest 
rows.
command: cat filtered.ann.vcf | grep -v "^#" | sort -nk 6 -r | head > topvariants.vcf

The top result has QUAL of 87098.3 and it has different consequences: upstream coding region, downstream coding region, protein coding region.
The next result also has similar effects and it has QUAL of 62724.2
For a lot of results chromosome is not found.

