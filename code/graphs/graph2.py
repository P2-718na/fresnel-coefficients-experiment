import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import numpy as np


#see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot for possible format strings

#load data
data=np.loadtxt("./data/sigma/run1-adjusted.csv")
x=data[:,0]
y=data[:,1]
ysigma=data[:,3]

def functionP(x,I_0,deltaTheta,n2):
   return I_0 * np.square(
       ((np.sqrt(1-np.square(((1/n2)*np.sin(np.radians(x-deltaTheta))))))-n2*np.cos(np.radians(x-deltaTheta)))
        /((np.sqrt(1-np.square(((1/n2)*np.sin(np.radians(x-deltaTheta))))))+n2*np.cos(np.radians(x-deltaTheta)))
)
def functionS(x,I_0,deltaTheta,n2):
   return I_0 * np.square((-n2*(np.sqrt(1-np.square(((1/n2)*np.sin(np.radians(x-deltaTheta))))))+np.cos(np.radians(x-deltaTheta)))/(n2*(np.sqrt(1-np.square(((1/n2)*np.sin(np.radians(x-deltaTheta))))))+np.cos(np.radians(x-deltaTheta))))


#fitted values
n2=1.490
deltaTheta=0
I_0=1350



#for plotting functions
functionX = np.arange(0, 90, 0.01)

#for calculating residual, swap between functionS and functionP
fitted_y = functionS(x,I_0,deltaTheta,n2)


fig=plt.figure()

#per no residui swappa queste due linee, devi anche levare le altre definizioni di ax0 e tutti i riferimenti a ax1
gs=gridspec.GridSpec(2,1,height_ratios=[4,1])
#ax0=plt.axes()

#graph
ax0=plt.subplot(gs[0])

dataplot=ax0.scatter(x,y,marker='o',s=3,color='red',label='Dati')


#swap between functionP and functionS
fitplot = ax0.plot(functionX,functionS(functionX,I_0,deltaTheta,n2),color='blue',linewidth='.5',label='Fit')


#funzione reale se la vuoi mettere alla fine, secondo me ha senso a quel punto farla a tratti o cose del genere
#realfunc = ax0.plot(functionX,functionP(functionX,I_0,deltaTheta,n2),color='blue',linewidth='.3',label='fit',ls='--')


#residual
ax1=plt.subplot(gs[1])
difference=np.subtract(fitted_y,y)
residual=ax1.plot(x,difference,label='Residuo',color='green',linewidth='.5')
dataplot=ax1.scatter(x,difference,marker='o',s=3,color='green')


#cosmetic
#idk if you want title?, boscherini dice che deve essere incluso nell'area del grafico, y da 0 a 1 è dentro il grafico
ax0.set_title('Intensità del fascio $\sigma$-polarizzato',x=0.5, y=0.85,fontdict={'fontsize': 11},backgroundcolor='white',bbox=dict(facecolor='white',edgecolor='black'))
lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax0.legend(lines, labels)

#se vuoi la griglia
ax0.grid(True,which='minor',linewidth=.2)
ax0.grid(True,which='major')


ax1.grid(True,which='minor',linewidth=.2)
ax1.grid(True,which='major')

#limiti sulle y se servono, forse va messo diverso x residui
ax0.set_ylim(0,1200)

ax1.set_xlim(0,90)
ax0.set_xlim(0,90)
ax1.set_ylim(-25,25)

#codice per grafico con residui
#plt.setp(ax0.get_xticklabels(),visible=False)
plt.subplots_adjust(hspace=.3)
#qui boscherini dice di mettere il simbolo dell'unità di misura, non so se scrivere deg o mettere °
ax1.set_xlabel("Angolo (deg)")
ax0.set_xlabel("Angolo (deg)")
#maybe V for volt instead of unità arbitraria, vedi punto 12 delle sue guidelines
ax0.set_ylabel("Intensità (un. arb.)")
ax1.set_ylabel("Residuo (un.arb)")
#1 minor tick between major ticks
ax1.xaxis.set_major_locator(MultipleLocator(5))
ax1.xaxis.set_major_formatter(FormatStrFormatter('%d'))
ax1.xaxis.set_minor_locator(MultipleLocator(1))
ax0.xaxis.set_major_locator(MultipleLocator(5))
ax0.xaxis.set_major_formatter(FormatStrFormatter('%d'))
ax0.xaxis.set_minor_locator(MultipleLocator(1))
ax1.tick_params(axis='both',direction='in',which='both')
ax0.tick_params(axis='both',direction='in',which='both')
ax0.tick_params('both', length=5, which='major',labelsize=9)
ax1.tick_params('both', length=5, which='major',labelsize=9)

#yticks
ax0.yaxis.set_major_locator(MultipleLocator(200))
ax0.yaxis.set_major_formatter(FormatStrFormatter('%d'))
ax0.yaxis.set_minor_locator(MultipleLocator(40))

#questi sono per l'asse del resiudo, vanno cambiati in base a quanto esce o quanto spazio abbimao, sempre metà minor del major se vuoi un tick in mezzo a ogni major couple
ax1.yaxis.set_major_locator(MultipleLocator(10))
ax1.yaxis.set_minor_locator(MultipleLocator(5))





#codice per grafico senza residui
#ax0.set_xlabel("Angolo (deg)")
#ax0.set_ylabel("Intensità (un. arb.)")
#ax0.xaxis.set_major_locator(MultipleLocator(10))
#ax0.xaxis.set_major_formatter(FormatStrFormatter('%d'))
#ax0.xaxis.set_minor_locator(MultipleLocator(2.5))
# ax0.xaxis.set_ticks(np.arange(start, end, stepsize))
# starty,endy=ax0.get_ylim()
# #step size for major ticks in y
# stepsizey=100
# ax0.yaxis.set_ticks(np.arange(starty, endy, stepsizey))
#ax0.tick_params(axis='both',direction='inout')





#latex backend
plt.savefig("./build/graphs/raw-sigma.pgf", bbox_inches='tight')

#normal png
plt.savefig("./build/graphs/raw-sigma.png", bbox_inches='tight')
