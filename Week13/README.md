wget "https://bx.bio.jhu.edu/data/cmdb-lab/week13_data.tar"
tar -xvf week13_data.tar

Download KronaTools-2.7 and place it in the current folder, untar it.
Run ./install.py, ./updateTaxonomy.sh, ./updataAccession.sh

Used piechartprocessing.py to creat KronaTools compatible text files

./KronaTools-2.7/scripts/ImportText.pl  piechart1*.txt

IN the first data (183), Enterococcus faecalis is the largest species and some
Actinobacteria are present but it changes in the next day (186). In 186, Actinobacteria is 
diminished and Enterococcus faecalis dominates even more. 188 and 189 are similar to 186.
IN 190 and 193  and 194 Staphylococcus increases, and in 197 Actinobacteria increases again.

Bins downloaded from the link 

Used grep to manually identify the taxonomy

Heatmap script
