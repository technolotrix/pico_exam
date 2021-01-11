
set terminal png

set style data histogram
set style fill solid border -1

set output "~/Desktop/pico_qa/tmp/histogram-test.png"

set title "Performance Test: 100 Requests and 10 Concurrencies"
set xlabel "Number of Requests"
set ylabel "Time (ms)"

set xrange [0:1000]
set yrange [0:1000]

binwidth=10
set boxwidth binwidth
bin(x,width)=width*floor(x/width)

plot "~/Desktop/pico_qa/tmp/histogram-.dat" using (bin($1,binwidth)):(1.0) smooth freq with boxes
