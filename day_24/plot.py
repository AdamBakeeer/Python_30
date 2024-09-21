import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot([0,1,2,3,4,5])
plt.show()
plt.savefig('output_plot.png')

random_data = np.random.binomial(n=10, p=0.5, size=1000)
# Plot histogram with Seabor
sns.histplot(random_data, kde=False) 
plt.savefig('up.png') # No need for hist=True
# Show plot
plt.show()