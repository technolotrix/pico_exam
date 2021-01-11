#!/usr/bin/gnuplot -persist

set style data histogram
set style fill solid border -1

set title "Performance Test: 100 Requests and 10 Concurrencies"
set xlabel "Number of Requests"
set ylabel "Time (ms)"

set xlabel "location"