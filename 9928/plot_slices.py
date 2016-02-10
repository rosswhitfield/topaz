#/usr/bin/python
import sys
sys.path.append("/opt/Mantid/bin")
from mantid.simpleapi import *
import numpy as np
import math
import matplotlib.pyplot as plt


workingdir="/SNS/users/rwp/9928/"
data=LoadMD(Filename=workingdir+'mirror.nxs',OutputWorkspace='data')
d=data.getSignalArray()
l=10
xx=np.linspace(-10,10,201)
yy=np.linspace(-l,l,201)
X,Y = np.meshgrid(xx,yy)


k=2
index=k*10+100
fig, ax = plt.subplots(figsize=(12,9))
plt.title('k='+str(k))
plt.xlabel('[H,0,0]')
plt.ylabel('[0,0,L]')
Z=np.ma.masked_invalid(d)
p = ax.pcolormesh(X,Y,Z, vmax=4e-7)
cb = fig.colorbar(p, ax=ax)
fig.show()


for k in range(10):
    index=k*10+100
    fig, ax = plt.subplots(figsize=(12,9))
    plt.title('Sr$_3$(Ru$_{(1-x)}$Mn$_x$)$_2$O$_7$ ($h$'+str(k)+'$l$)')
    plt.xlabel('[H,'+str(k)+',0]')
    plt.ylabel('[0,'+str(k)+',L]')
    p = ax.pcolormesh(X,Y,np.ma.masked_invalid(d[:,index,:]), vmin=0, vmax=4e-7)
    cb = fig.colorbar(p, ax=ax)
    fig.savefig('Sr3Ru2O7_l'+str(l)+'_h'+str(k)+'l.png')
    fig.clf()



workingdir="/SNS/users/rwp/9928/20/"
data=LoadMD(Filename=workingdir+'mirror.nxs',OutputWorkspace='data')
d=data.getSignalArray()
l=20
xx=np.linspace(-10,10,201)
yy=np.linspace(-l,l,201)
X,Y = np.meshgrid(xx,yy)
for k in range(10):
    index=k*10+100
    fig, ax = plt.subplots(figsize=(12,9))
    plt.title('Sr$_3$(Ru$_{(1-x)}$Mn$_x$)$_2$O$_7$ ($h$'+str(k)+'$l$)')
    plt.xlabel('[H,'+str(k)+',0]')
    plt.ylabel('[0,'+str(k)+',L]')
    p = ax.pcolormesh(X,Y,np.ma.masked_invalid(d[:,index,:]), vmin=0, vmax=4e-7)
    cb = fig.colorbar(p, ax=ax)
    #fig.show()
    fig.savefig('Sr3Ru2O7_l'+str(l)+'_h'+str(k)+'l.png')
    fig.clf()



workingdir="/SNS/users/rwp/9928/40/"
data=LoadMD(Filename=workingdir+'mirror.nxs',OutputWorkspace='data')
d=data.getSignalArray()
l=40
xx=np.linspace(-10,10,201)
yy=np.linspace(-l,l,201)
X,Y = np.meshgrid(xx,yy)
for k in range(10):
    index=k*10+100
    fig, ax = plt.subplots(figsize=(12,9))
    plt.title('Sr$_3$(Ru$_{(1-x)}$Mn$_x$)$_2$O$_7$ ($h$'+str(k)+'$l$)')
    plt.xlabel('[H,'+str(k)+',0]')
    plt.ylabel('[0,'+str(k)+',L]')
    p = ax.pcolormesh(X,Y,np.ma.masked_invalid(d[:,index,:]), vmin=0, vmax=4e-7)
    cb = fig.colorbar(p, ax=ax)
    #fig.show()
    fig.savefig('Sr3Ru2O7_l'+str(l)+'_h'+str(k)+'l.png')
    fig.clf()



