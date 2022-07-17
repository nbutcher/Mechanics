import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,11,1)
k = 2

F = k * x

plt.plot(x,F)
plt.xlabel('Displacement')
plt.ylabel('Force required to displace the spring')
#plt.tick_params(
#        axis='x',
#        which='both',
#        bottom='False',
#        top='False',
#        labelbottom='False')
#plt.tick_params(
#        axis='y',
#        which='both',
#        left='False',
#        right='False',
#        labelleft='False')
plt.xticks([])
plt.yticks([])
plt.xlim(0,10)
plt.ylim(0,20)
plt.savefig('force_spring.png')
