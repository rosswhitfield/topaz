#/usr/bin/python
import sys
sys.path.append("/opt/Mantid/bin")
from mantid.simpleapi import *
workingdir="/SNS/users/rwp/9928/"
UBfile="/SNS/users/rwp/9928/TOP_8005_8035.mat"

runs=range(8005,8035) #skip 7997, too low statistics
#runs=range(8016,8017) #skip 7997, too low statistics

#Load(Filename='/SNS/users/rwp/9928/rawVan_smooth_finestep',OutputWorkspace='rawVan')
#Rebin(InputWorkspace='rawVan',OutputWorkspace='rawVan',Params="1.84,0.005,10")
#ConvertUnits(InputWorkspace='rawVan',OutputWorkspace='rawVan',Target='Momentum')
#CropWorkspace(InputWorkspace='rawVan',OutputWorkspace='rawVan',XMin='1.84',XMax='10')
#LoadIsawUB(InputWorkspace='rawVan',Filename=UBfile)

for r in runs:
    print "************* processing run "+str(r)+" ***********************"
    #Load("TOPAZ_"+str(r),OutputWorkspace="raw")
    #FilterBadPulses(InputWorkspace='raw',OutputWorkspace='raw')
    #MaskBTP(Workspace="raw",Tube="0-3,252-255")
    #MaskBTP(Workspace="raw",Pixel="0-3,252-255")
    #ConvertUnits(InputWorkspace='raw',OutputWorkspace='raw',Target='Momentum')
    #CropWorkspace(InputWorkspace="raw",XMin='1.84',XMax='10',OutputWorkspace="raw")
    #LoadIsawUB(InputWorkspace="raw",Filename=UBfile)
    #data=ConvertToMD(InputWorkspace="raw",QDimensions='Q3D',dEAnalysisMode='Elastic', Q3DFrames='HKL',
    #    QConversionScales='HKL',LorentzCorrection='1', MinValues='-10.1,-10.1,-20.2',MaxValues='10.1,10.1,20.2')
    data=LoadMD(Filename=workingdir+"TOPAZ_"+str(r)+"_MDE.nxs",OutputWorkspace='raw')
    dataRebinned=BinMD(InputWorkspace=data,AxisAligned='0',
	    BasisVector0='[H,0,0],in 1.178 A^-1,1,0,0',BasisVector1='[0,K,0],in 1.178 A^-1,0,1,0',
	    BasisVector2='[0,0,L],in 1.644 A^-1,0,0,1',OutputExtents='-10.025,10.025,-10.025,10.025,-20.05,20.05',
	    OutputBins='401,401,401',Parallel='1')
    #SaveMD(data,workingdir+"TOPAZ_"+str(r)+"_MDE.nxs")
    #SaveMD(dataRebinned,workingdir+"TOPAZ_"+str(r)+"_MDH.nxs")
    if mtd.doesExist('dataHisto'):
        dataHisto=dataHisto+dataRebinned
    else:
	    dataHisto=CloneMDWorkspace(dataRebinned)
    print "************* processing vanadium for run "+str(r)+" ***********************"
    #runObj=data.getExperimentInfo(0).run()
    #CreateSingleValuedWorkspace(runObj.getProtonCharge(),OutputWorkspace="PC")
    #Multiply(LHSWorkspace="rawVan",RHSWorkspace="PC",OutputWorkspace="van")
    #MaskDetectors(Workspace="van",MaskedWorkspace="raw")
    #AddSampleLog(Workspace='van',LogName='phi',LogText=str(float(runObj['phi'].value)),LogType='Number Series')
    #AddSampleLog(Workspace='van',LogName='omega',LogText=str(float(runObj['omega'].value)),LogType='Number Series')
    #SetGoniometer(Workspace='van',Goniometers='Universal')
    #ConvertToMD(InputWorkspace='van',OutputWorkspace='vanMDE',QDimensions='Q3D',
    #    dEAnalysisMode='Elastic',Q3DFrames='HKL',QConversionScales='HKL',LorentzCorrection='1',
    #    MinValues='-10.1,-10.1,-20.2',MaxValues='10.1,10.1,20.2',SplitInto='2,2,2')
    LoadMD(Filename=workingdir+"VAN_"+str(r)+"_MDE.nxs",OutputWorkspace='vanMDE')
    BinMD(InputWorkspace='vanMDE',AxisAligned='0',BasisVector0='[H,0,0],in 1.178 A^-1,1,0,0',BasisVector1='[0,K,0],in 1.178 A^-1,0,1,0',
        BasisVector2='[0,0,L],in 1.644 A^-1,0,0,1',OutputExtents='-10.025,10.025,-10.025,10.025,-20.05,20.05',
        OutputBins='401,401,401',Parallel='1',OutputWorkspace='vanMDH')
    #SaveMD('vanMDE',workingdir+"VAN_"+str(r)+"_MDE.nxs")
    #SaveMD('vanMDH',workingdir+"VAN_"+str(r)+"_MDH.nxs")
    if mtd.doesExist('vanHisto'):
        vanHisto=PlusMD(LHSWorkspace="vanHisto",RHSWorkspace="vanMDH")
    else:
        vanHisto=CloneMDWorkspace("vanMDH")

SaveMD("vanHisto",workingdir+"vanHisto_401.nxs")
SaveMD("dataHisto",workingdir+"dataHisto_401.nxs") 
#symmetryzation
DivideMD(LHSWorkspace="dataHisto",RHSWorkspace="vanHisto",OutputWorkspace="out")
SaveMD("out",workingdir+"out_401.nxs")

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
SaveMD("symm",workingdir+"mirror_401.nxs")

