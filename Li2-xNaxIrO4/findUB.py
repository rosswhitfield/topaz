LoadEventNexus(Filename='/SNS/TOPAZ/2013_1_12_SCI/0/7421/NeXus/TOPAZ_7421_event.nxs', OutputWorkspace='TOPAZ_7421')
ConvertToMD(InputWorkspace='TOPAZ_7421', QDimensions='Q3D', dEAnalysisMode='Elastic', Q3DFrames='Q_sample', OutputWorkspace='TOPAZ_7241_md', MinValues='-25,-25,-25', MaxValues='25,25,25', SplitInto='2', SplitThreshold=50, MaxRecursionDepth=13, MinRecursionDepth=7)
FindPeaksMD(InputWorkspace='TOPAZ_7241_md', PeakDistanceThreshold=0.3, MaxPeaks=50, DensityThresholdFactor=1000, OutputWorkspace='peaks')
FindUBUsingFFT(PeaksWorkspace='peaks', MinD=5, MaxD=10)
ShowPossibleCells('peaks')
SelectCellOfType(PeaksWorkspace='peaks', CellType='Monoclinic', Centering='C', Apply=True)
SaveIsawUB(InputWorkSpace='peaks',Filename='/SNS/users/rwp/TOPAZ_7421.mat')

#Convert to HKL using found UB.
CopySample(InputWorkspace='peaks', OutputWorkspace='TOPAZ_7421', CopyName=False, CopyMaterial=False, CopyEnvironment=False, CopyShape=False)
CropWorkspace(InputWorkspace='TOPAZ_7421', OutputWorkspace='TOPAZ_7421', XMin=100)
ConvertToMD(InputWorkspace='TOPAZ_7421', QDimensions='Q3D', dEAnalysisMode='Elastic', Q3DFrames='HKL', QConversionScales='HKL', OutputWorkspace='TOPAZ_7421_hkl')
