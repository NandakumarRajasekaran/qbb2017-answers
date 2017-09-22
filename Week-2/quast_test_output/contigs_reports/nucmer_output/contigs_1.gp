set terminal canvas jsdir ""
set output "/Users/cmdb/qbb2017-answers/Week-2/quast_test_output/contigs_reports/nucmer_output/contigs_1.html"
set ytics ( \
 "0" 0, \
 "800" 800, \
 "1600" 1600, \
 "2400" 2400, \
 "3200" 3200, \
 "4000" 4000, \
 "4800" 4800, \
 "5600" 5600, \
 "6400" 6400, \
 "" 6710 \
)
set size 1,1
set grid
set key outside bottom right
set border 0
set tics scale 0
set xlabel "Reference" noenhanced
set ylabel "Assembly" noenhanced
set format "%.0f"
set xrange [1:*]
set yrange [1:6710]
set linestyle 1  lt 1 lc rgb "red" lw 3 pt 7 ps 0.5
set linestyle 2  lt 3 lc rgb "blue" lw 3 pt 7 ps 0.5
set linestyle 3  lt 2 lc rgb "yellow" lw 3 pt 7 ps 0.5
plot \
 "/Users/cmdb/qbb2017-answers/Week-2/quast_test_output/contigs_reports/nucmer_output/contigs_1.fplot" title "FWD" w lp ls 1, \
 "/Users/cmdb/qbb2017-answers/Week-2/quast_test_output/contigs_reports/nucmer_output/contigs_1.rplot" title "REV" w lp ls 2
