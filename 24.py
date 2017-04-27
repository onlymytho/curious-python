import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


plt.plot([1, 2, 3, 2])


x = range(0, 100)
y = [v*v for v in x]
plt.plot(x, y, 'k.')



plt.show()
