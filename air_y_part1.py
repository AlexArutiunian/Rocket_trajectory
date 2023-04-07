import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

# Plot and save y(t) for fixed v0, α and varying
# resistance coefficient k.

# Triginometry {{{
def cos(x): return round( np.cos( np.radians(x) ), 10 )
def sin(x): return round( np.sin( np.radians(x) ), 10 )
def sins(x): return round( np.sin( np.radians(x) )**2, 10 )
def asin(x): return np.degrees( np.arcsin(x) )
def tg(x): return round( np.tan( np.radians(x) ), 10 )
def atg(x): return np.degrees( np.arctan(x) )
#}}}
# Plot setup {{{
rcParams['font.size'] = 16.
rcParams['text.usetex'] = True
rc('text.latex', preamble=r'\usepackage[T2A]{fontenc} \usepackage[utf8]{inputenc} \usepackage{bm}')

rc('axes', linewidth=1.2)
rc('xtick.major', size=4, width=1.1)
rc('ytick.major', size=4, width=1.1)
fig, ax = plt.subplots()
fig.subplots_adjust(left=.15, bottom=.15, right=.95, top=.85)
#}}}

v0 = 0
a  = 89
m  = 1
k  = 0.4
g  = 10

times = np.linspace(0,1.1,1000)
ks = np.arange(0.0001,1.1,0.005) # Set larger step instead of 0.005 to reduce images number
ms = np.arange(0.1, 5.0, 0.1)


with open('coor_y.txt', 'w') as f:

    for m in ms:
        y=[]
        for t in times:
            y = np.append( y, v0*t - g*t**2/2)
        ax.plot(times, y, ls=':', label='$F_\\textrm{сопр}=0$')
        
        y=[]
        for t in times:
            y = np.append( y, (v0+m/k*(g- 30/m)) * m/k * (np.exp(-k*t/m)-1) - (g - 30/m)*m/k*t)
            
                    
        t = 1            
        
        f.write(str("{:.2f}".format((v0+m/k*(g- 30/m)) * m/k * (np.exp(-k*t/m)-1) - (g - 30/m)*m/k*t)))
        f.write('\n')      
        
        ax.plot(times, y, label='$F_\\textrm{сопр}=kv$')
        
        ax.set_xlabel('$t$ [\\textrm{с}]')
        ax.set_ylabel('$y$ [\\textrm{м}]')

        ax.plot([], [], ' ', label='$k={}~$'.format( "{:.2f}".format(k) )+'\\textrm{кг/с}')
        ax.plot([], [], ' ', label='$m={}~$'.format( "{:.2f}".format(m) )+'\\textrm{кг}')
        ax.plot([], [], ' ', label='$v_0={}~$'.format( "{:.0f}".format(v0) )+'\\textrm{м/с}')
        ax.plot([], [], ' ', label='$\\alpha={}$'.format( "{:.0f}".format(a) )+'$^\circ$')
        ax.legend(markerscale=0, handletextpad=0.4, loc='center',
                    bbox_to_anchor=(0.5, 1.15), ncol=3, columnspacing=0.0)
        ax.grid()

        plt.savefig('var_m_with_E/y_' + rf'{m:.2f}.png', bbox_inches='tight')
        plt.cla()