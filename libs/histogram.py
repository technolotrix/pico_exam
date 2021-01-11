import sys

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

if len(sys.argv) < 2:
    print('Usage: ' + sys.argv[0] + ' <filename>')
    sys.exit(1)

inputfile = str(sys.argv[1])

f = np.loadtxt(inputfile,
    skiprows=1, usecols=8, unpack='False')

print("Creating histogram for file {}".format(inputfile))

bins = [10 * n for n in range(100)]

plt.hist(f, histtype='bar', bins = bins)
plt.xlabel('Response time (ms)')
plt.ylabel('Number of Requests')
plt.title('Distribution of POST request response time')
plt.legend()
plt.show()
