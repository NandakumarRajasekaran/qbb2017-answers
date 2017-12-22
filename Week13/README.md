wget "https://bx.bio.jhu.edu/data/cmdb-lab/week13_data.tar"
tar -xvf week13_data.tar

Download KronaTools-2.7 and place it in the current folder, untar it.
Run ./install.py, ./updateTaxonomy.sh, ./updataAccession.sh

Used piechartprocessing.py to creat KronaTools compatible text files

./KronaTools-2.7/scripts/ImportText.pl  piechart1*.txt

Q1:IN the first data (183), Enterococcus faecalis is the largest species and some
Actinobacteria are present but it changes in the next day (186). In 186, Actinobacteria is 
diminished and Enterococcus faecalis dominates even more. 188 and 189 are similar to 186.
IN 190 and 193  and 194 Staphylococcus increases, and in 197 Actinobacteria increases again.

Bins downloaded from the link 

Q2: We can probably compare the contigs to known sequence databases to get an idea of the species. We can also use sequence homology to infer closely related species. We can also integrate some sort of classification (like k means or other algorithms) to group contigs

Q3: We downloaded 8 . We did not use metaBat


Used grep to manually identify the taxonomy

Q4: Manual identification may not reveal outliers or exceptions. For example, bin 8 can be clssified into multiple taxonomies. We could rather quantitatively compare all seqeunces in each bin and compare them with taxonomy using a python script.

Heatmap script

Q5: Heatmap and Read Taxonomy distributions give similar results. However the Krona Visualizations gave much more detailed info on all species compositions but heatmap reveals general trends