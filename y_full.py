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
times1 = np.linspace(1.1,15,1000)
times_full = np.linspace(0,15,2000)
ks = np.arange(0.0001,1.1,0.005) # Set larger step instead of 0.005 to reduce images number
ms = np.arange(0.1, 5.0, 0.1)


with open('test/coor_y.txt', 'r') as f:
    y_0 = f.readlines()

i = 0

while i != 48:
    
    y=[]
    for t in times:
        y = np.append( y, (v0+m/k*(g- 30/m)) * m/k * (np.exp(-k*t/m)-1) - (g - 30/m)*m/k*t)
        
    for t in times1:
        v0 = (ms[i] * (g - 30/ms[i]) / k)*np.exp(-k/ms[i] * t) - (g - 30/ms[i]) * ms[i] / k
        y = np.append( y, -(v0+ms[i]/k*(g/ms[i])) * ms[i]/k * (np.exp(-k*t/ms[i])-1) - (g/ms[i])*ms[i]/k*t + float(y_0[i]))          
            
    
    ax.plot(times_full, y, label='$F_\\textrm{сопр}=kv$')
    
    ax.set_xlabel('$t$ [\\textrm{с}]')
    ax.set_ylabel('$y$ [\\textrm{м}]')

    ax.plot([], [], ' ', label='$k={}~$'.format( "{:.2f}".format(k) )+'\\textrm{кг/с}')
    ax.plot([], [], ' ', label='$m={}~$'.format( "{:.2f}".format(ms[i]) )+'\\textrm{кг}')
    ax.plot([], [], ' ', label='$v_0={}~$'.format( "{:.0f}".format(v0) )+'\\textrm{м/с}')
    ax.plot([], [], ' ', label='$\\alpha={}$'.format( "{:.0f}".format(a) )+'$^\circ$')
    ax.legend(markerscale=0, handletextpad=0.4, loc='center',
                bbox_to_anchor=(0.5, 1.15), ncol=3, columnspacing=0.0)
    ax.grid()

    plt.ylim([0, 300])
    plt.savefig('var_m_full/y_' + rf'{ms[i]:.2f}.png', bbox_inches='tight')
    plt.cla()

    i += 1