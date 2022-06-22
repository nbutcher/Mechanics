import numpy as np
import matplotlib.pyplot as plt

t = np.array([0,1,2,3,4])
a = np.array([9,7,5,3,1])
v = np.array([-4,4,10,14,16])

tfunc = np.arange(0,4.01,0.01)
vfunc = -4 + 9 * tfunc - 0.5 * 2. * tfunc**2

plt.scatter(t,a,c='blue')
plt.plot(t,a,c='blue')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s/s)')
plt.grid(which='both')
plt.savefig('example_accel')
plt.clf()

plt.scatter(t,v,c='blue')
plt.plot(tfunc,vfunc,c='blue')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid(which='both')
plt.savefig('example_vel')
plt.clf()
