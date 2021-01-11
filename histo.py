#!/usr/bin/env python3
#coding=utf8
from pygnuplot import gnuplot
import pandas as pd

datafile = pd.read_csv('~/Desktop/pico_qa/tmp/histogram-.dat', index_col = 0, sep='\t', comment='#')
g = gnuplot.Gnuplot()
g.set(terminal = 'pngcairo transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 ',
        output = '"histogram-test-1.png"',
        key = 'fixed right top vertical Right noreverse noenhanced autotitle nobox',
        style = 'data linespoints',
        datafile = ' missing "-"',
        xtics = 'border in scale 1,0.5 nomirror rotate by -45 autojustify norangelimit',
        title = '"US immigration from Europe by decade"')
g.plot_data(df, 'using 2:xtic(1), for [i=3:22] "" using i ')