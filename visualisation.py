import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,5,4,2,6,2,8,9,10]
z=  [2,3,2,8,5,6,3,9,1,6]

plt.plot(x, y, linewidth=2.0)
plt.show()
plt.scatter(x, y)
plt.show()
plt.bar(x, y)
plt.show()
plt.stackplot(x, y)
plt.show()

plt.pie(x, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(x, y, z)
plt.show()

