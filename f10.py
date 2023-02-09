import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


mill = 1000000

# Initializing vector
v = np.random.lognormal(0, 1, mill)

plt.xlabel("value")
plt.ylabel("percentage")
plt.title("Empirical CDF of a million log-normal distributed values")
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
x = np.sort(v)
y = np.arange(len(x))/float(len(x))
plt.plot(x, y)
#plt.show()                        #use plt.show to show figure in output window
plt.savefig('ecdf.png', dpi=300)    #use plt.savefig to save figure to file

print(np.percentile(v, 50))
