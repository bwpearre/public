import numpy as np
import pysd, simpy
import pdb
import matplotlib.pyplot as plt
from matplotlib import cm
#import matplotlib
#matplotlib.use("TkAgg")

model = pysd.read_vensim('scooters.mdl')
print(model)

xx = np.linspace(1, 40, 15) # scooter speed limit
yy = np.linspace(0.4, 1, 15) # infrastructure responsiveness

xv, yv = np.meshgrid(xx, yy, indexing='xy')
zv = np.empty_like(xv)

#pdb.set_trace()

for x in range(len(xx)):
    for y in range(len(yy)):
        stocks = model.run(params={'scootershare introduced': 1000,
                                   '"speed(bike)"': 14,
                                   '"capability(bike)"': yv[x,y],
                                   '"speed(scooter)"': xv[x,y],
                                   'µmobility infrastructure investment responsiveness': 0.0018},
                           return_timestamps=[10000])

        zv[x,y] = stocks['"∆ life minutes / day"'].values[0]
        #print(f'Iter {i}, compliance {compliances[i]}, prob {prb[i]}')

#plt.figure('foo')
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
#plt.contourf(xx, yy, zv)
surf = ax.plot_surface(xv, yv, zv, cmap=cm.jet)

fig.colorbar(surf, pad=0.1)
#plt.axis('scaled')
#colorbar = plt.colorbar()
#colorbar.ax.set_title('Pr(bike)')
ax.set_xlabel('scooter speed limit')
# ax.set_ylabel('infrastructure responsiveness')
ax.set_ylabel('bicycle capability')
ax.set_zlabel('final ∆ life minutes / day')
#plt.zlabel('Pr(bike)')
plt.show()

'''
plt.figure('probs')
stocks['"Pr(bike)"'].plot()
#stocks['"delta life-minutes / day: all causes"'].plot()
stocks['compliance'].plot()
plt.title("Probability of biking")
plt.legend(['Pr(bike)', 'compliance'])
plt.show()
'''


#pdb.set_trace()