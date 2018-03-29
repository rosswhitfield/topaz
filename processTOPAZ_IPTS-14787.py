instrument_name ='TOPAZ'
datadir = '/SNS/TOPAZ/IPTS-14787/data/'

#Vanadium and calibration files
geometryfile='/SNS/TOPAZ/IPTS-14787/shared/calibration/TOPAZ_2015B.DetCal'
calibrationdir ='/SNS/TOPAZ/IPTS-14787/shared/calibration/'

#UB matrix
UBfile='/SNS/TOPAZ/IPTS-14787/shared/100K/TOPAZ_12413_R.mat'    # need to add integration directory
#run numbers
runs=range(12413,12414)

#vanadium processing
sa=Load(calibrationdir+'solidAngle12387.nxs')
flux=Load(calibrationdir+'spectra12387.nxs')

data=Load(datadir+instrument_name +str(runs[0]))
LoadIsawDetCal(InputWorkspace=data, Filename=geometryfile)
MaskDetectors(Workspace=data,MaskedWorkspace=sa)
data1=ConvertUnits(InputWorkspace=data,Target='Momentum')
data2=CropWorkspace(InputWorkspace=data1,XMin='1.5',XMax='32.0')
data=Rebin(InputWorkspace=data2,Params='1.5,32,32.0')
LoadIsawUB(InputWorkspace=data,Filename=UBfile)
md=ConvertToMD(InputWorkspace=data,
               QDimensions="Q3D",
               dEAnalysisMode="Elastic",
               Q3DFrames="HKL",
               QConversionScales="HKL",
               MinValues="-5.01,-5.01,-15.025",
               Maxvalues="5.01,5.01,15.025")

dataMD,normMD=MDNormSCD(InputWorkspace=md,FluxWorkspace=flux,SolidAngleWorkspace=sa,
          AlignedDim0="[H,0,0],-5.01,5.01,251",
	      AlignedDim1="[0,K,0],-5.01,5.01,251",
	      AlignedDim2="[0,0,L],-15.025,15.025,301")

normalized=DivideMD(dataMD,normMD)
