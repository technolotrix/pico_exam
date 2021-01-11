import matplotlib.pyplot as plt
import numpy as np
import matplotlib

inputfile = '/Users/nicoleawesome/Desktop/pico_qa/tmp/histogram-2021-01-11_01-14-58.dat'

f = np.loadtxt(inputfile,
    skiprows=1, usecols=8, unpack='False')

bins = [10 * n for n in range(100)]

plt.hist(f, histtype='bar', bins = bins)
plt.xlabel('Response time (ms)')
plt.ylabel('Number of Requests')
plt.title('Distribution of POST request response time')
plt.legend()
plt.show()