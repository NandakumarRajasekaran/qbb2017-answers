set terminal canvas jsdir ""
set output "/Users/cmdb/qbb2017-answers/Week-2/quast_test_output/contigs_reports/nucmer_output/spades_high_contigs.html"
set size 1,1
set grid
set key outside bottom right
set border 5
set tics scale 0
set xlabel "Reference" noenhanced
set ylabel "NODE_1_length_100000_cov_225.046" noenhanced
set format "%.0f"
set xrange [1:*]
set yrange [1:100000]
set linestyle 1  lt 1 lc rgb "red" lw 3 pt 7 ps 0.5
set linestyle 2  lt 3 lc rgb "blue" lw 3 pt 7 ps 0.5
set linestyle 3  lt 2 lc rgb "yellow" lw 3 pt 7 ps 0.5
plot \
 "/Users/cmdb/qbb2017-answers/Week-2/quast_test_output/contigs_reports/nucmer_output/spades_high_contigs.fplot" title "FWD" w lp ls 1, \
 "/Users/cmdb/qbb2017-answers/Week-2/quast_test_output/contigs_reports/nucmer_output/spades_high_contigs.rplot" title "REV" w lp ls 2
