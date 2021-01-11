import os

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

inputfile = str(os.environ.get('OUTPUTFILE'))

f = np.loadtxt(inputfile,
    skiprows=1, usecols=8, unpack='False')

bins = [10 * n for n in range(100)]

plt.hist(f, histtype='bar', bins = bins)
plt.xlabel('Response time (ms)')
plt.ylabel('Number of Requests')
plt.title('Distribution of POST request response time')
plt.legend()
plt.show()