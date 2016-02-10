#/usr/bin/python
import sys
sys.path.append("/opt/Mantid/bin")
from mantid.simpleapi import *
workingdir="/SNS/users/rwp/9928/20/"
UBfile=workingdir+"TOP_8005_8035.mat"

dataHisto=LoadMD(OutputWorkspace="vanHisto",Filename=workingdir+"vanHisto.nxs")
vanHisto=LoadMD(OutputWorkspace="dataHisto",Filename=workingdir+"dataHisto.nxs") 

#symmetryzation
data_array=dataHisto.getSignalArray()
van_array=vanHisto.getSignalArray()
data_array=data_array[:,:,:]+data_array[::-1,::1,::1]
data_array=data_array[:,:,:]+data_array[::1,::-1,::1]
data_array=data_array[:,:,:]+data_array[::1,::1,::-1]
van_array=van_array[:,:,:]+van_array[::-1,::1,::1]
van_array=van_array[:,:,:]+van_array[::1,::-1,::1]
van_array=van_array[:,:,:]+van_array[::1,::1,::-1]
dataHisto.setSignalArray(data_array)
vanHisto.setSignalArray(van_array)
DivideMD(LHSWorkspace="dataHisto",RHSWorkspace="vanHisto",OutputWorkspace="symm")
SaveMD("symm",workingdir+"mirror.nxs")

