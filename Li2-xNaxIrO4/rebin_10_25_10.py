#/usr/bin/python
import sys
sys.path.append("/opt/Mantid/bin")
from mantid.simpleapi import *
workingdir="/SNS/users/rwp/Li2-xNaxIrO4/smooth_van/"
runs=range(7421,7449)


for r in runs:
    datai=LoadMD(workingdir+"15_25_15/TOPAZ_"+str(r)+"_MDE.nxs")
    datai_rebinned=BinMD(InputWorkspace=datai,AxisAligned='0',
	    BasisVector0='[H,0,0],in 1.178 A^-1,1,0,0',BasisVector1='[0,K,0],in 1.178 A^-1,0,1,0',
	    BasisVector2='[0,0,L],in 1.644 A^-1,0,0,1',OutputExtents='-10.05,10.05,-25.125,25.125,-10.05,10.05',
	    OutputBins='201,201,201',Parallel='1')
    if mtd.doesExist('data_histo'):
	    PlusMD(LHSWorkspace="data_histo",RHSWorkspace=datai_rebinned,OutputWorkspace="data_histo")
    else:
	    CloneMDWorkspace(datai_rebinned,OutputWorkspace="data_histo")
    vani=LoadMD(workingdir+"15_25_15/VAN_"+str(r)+"_MDE.nxs")
    vani_rebinned=BinMD(InputWorkspace=vani,AxisAligned='0',
	    BasisVector0='[H,0,0],in 1.178 A^-1,1,0,0',BasisVector1='[0,K,0],in 1.178 A^-1,0,1,0',
	    BasisVector2='[0,0,L],in 1.644 A^-1,0,0,1',OutputExtents='-10.05,10.05,-25.125,25.125,-10.05,10.05',
	    OutputBins='201,201,201',Parallel='1')
    if mtd.doesExist('van_histo'):
	    PlusMD(LHSWorkspace="van_histo",RHSWorkspace=vani_rebinned,OutputWorkspace="van_histo")
    else:
	    CloneMDWorkspace(vani_rebinned,OutputWorkspace="van_histo")

SaveMD("van_histo",workingdir+"10_25_10/vanHisto.nxs")
SaveMD("data_histo",workingdir+"10_25_10/dataHisto.nxs") 
#symmetryzation
#data_histo=mtd["data_histo"]
#van_histo=mtd["van_histo"]
#data_array=data_histo.getSignalArray()
#van_array=van_histo.getSignalArray()
#data_array=data_array[:,:,:]+data_array[::1,::-1,::-1]#+data_array[::-1,::1,::-1]+data_array[::-1,::-1,::1]
#van_array=van_array[:,:,:]+van_array[::1,::-1,::-1]#+van_array[::-1,::1,::-1]+van_array[::-1,::-1,::1]
#data_histo.setSignalArray(data_array)
#van_histo.setSignalArray(van_array)
DivideMD(LHSWorkspace="data_histo",RHSWorkspace="van_histo",OutputWorkspace="out")
SaveMD("out",workingdir+"10_25_10/out.nxs")
