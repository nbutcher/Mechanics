import numpy as np
import matplotlib.pyplot as plt

tlist = np.arange(0,7)
xlist = tlist * 2 - 2
vlist = np.ones(7) * 2.
print(tlist)
print(xlist)
print(vlist)

plt.plot(tlist,xlist)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(which="both")
plt.title("Position vs. Time")
plt.savefig("position1.png")
plt.clf()

plt.plot(tlist,vlist)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(which="both")
plt.ylim(0,4)
plt.title("Velocity vs. Time")
plt.savefig("velocity1.png")
plt.clf()
