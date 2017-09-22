set terminal canvas jsdir ""
set output "/Users/cmdb/qbb2017-answers/Week-2/quast_test_output/contigs_reports/nucmer_output/contigs_2.html"
set ytics ( \
 "0" 0, \
 "700" 700, \
 "1400" 1400, \
 "2100" 2100, \
 "2800" 2800, \
 "3500" 3500, \
 "4200" 4200, \
 "4900" 4900, \
 "" 5460 \
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
set yrange [1:5460]
set linestyle 1  lt 1 lc rgb "red" lw 3 pt 7 ps 0.5
set linestyle 2  lt 3 lc rgb "blue" lw 3 pt 7 ps 0.5
set linestyle 3  lt 2 lc rgb "yellow" lw 3 pt 7 ps 0.5
plot \
 "/Users/cmdb/qbb2017-answers/Week-2/quast_test_output/contigs_reports/nucmer_output/contigs_2.fplot" title "FWD" w lp ls 1, \
 "/Users/cmdb/qbb2017-answers/Week-2/quast_test_output/contigs_reports/nucmer_output/contigs_2.rplot" title "REV" w lp ls 2