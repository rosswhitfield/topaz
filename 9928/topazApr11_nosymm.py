#/usr/bin/python
import sys
sys.path.append("/opt/Mantid/bin")
from mantid.simpleapi import *
workingdir="/SNS/users/rwp/9928/"
UBfile=workingdir+"TOP_8005_8035.mat"

LoadMD(OutputWorkspace="vanHisto",Filename=workingdir+"vanHisto.nxs")
LoadMD(OutputWorkspace="dataHisto",Filename=workingdir+"dataHisto.nxs") 
DivideMD(LHSWorkspace="dataHisto",RHSWorkspace="vanHisto",OutputWorkspace="nosymm")
SaveMD("nosymm",workingdir+"nosymm.nxs")
