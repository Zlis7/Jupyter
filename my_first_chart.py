# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt


ox = np.arange(0.,1.,0.05)
oy = np.sin(2*np.pi*ox)

plt.text(0.6,0.5,r'$y = $sin(x)',fontsize=20,bbox={'facecolor':'yellow','alpha':0.4})
plt.text(0.4,-0.5,'*')
plt.text(0.2,-0.75,'*')
plt.grid(True)


plt.plot([0,0.1,0.2,0.3,0.4],[1,2,3,4,5],'ro')
plt.plot(ox,oy,'y-.')
plt.legend(['*', 'y = sin(x)'])
