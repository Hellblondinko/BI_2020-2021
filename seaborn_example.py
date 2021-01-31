import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

the_array = np.zeros(shape=(500,10))
for i in range(10):
    the_array[:,i] = np.random.normal(loc=i, size=(500,))

sns.set_style("darkgrid", { "axes.facecolor": ".9"})

sns.violinplot(data=[d for d in the_array.T])

plt.show()

