LoadEventNexus(Filename='/SNS/TOPAZ/2013_1_12_SCI/0/7421/NeXus/TOPAZ_7421_event.nxs', OutputWorkspace='TOPAZ_7421', LoadMonitors=True, MonitorsAsEvents=True)
ConvertToMD(InputWorkspace='TOPAZ_7421', QDimensions='Q3D', dEAnalysisMode='Elastic', Q3DFrames='Q_sample', OutputWorkspace='TOPAZ_7241_md', MinValues='-25,-25,-25', MaxValues='25,25,25', SplitInto='2', SplitThreshold=50, MaxRecursionDepth=13, MinRecursionDepth=7)
FindPeaksMD(InputWorkspace='TOPAZ_7241_md', PeakDistanceThreshold=0.37680000000000002, MaxPeaks=50, DensityThresholdFactor=100, OutputWorkspace='peaks')
FindUBUsingFFT(PeaksWorkspace='peaks', MinD=3, MaxD=15, Tolerance=0.12)
CopySample(InputWorkspace='peaks', OutputWorkspace='TOPAZ_7241_md', CopyName=False, CopyMaterial=False, CopyEnvironment=False, CopyShape=False)
CopySample(InputWorkspace='peaks', OutputWorkspace='TOPAZ_7421', CopyName=False, CopyMaterial=False, CopyEnvironment=False, CopyShape=False)
FindPeaksMD(InputWorkspace='TOPAZ_7241_md', PeakDistanceThreshold=0.56520000000000004, MaxPeaks=50, DensityThresholdFactor=200, OutputWorkspace='peaks')
FindUBUsingFFT(PeaksWorkspace='peaks', MinD=5, MaxD=10, Tolerance=0.12)
CopySample(InputWorkspace='peaks', OutputWorkspace='TOPAZ_7241_md', CopyName=False, CopyMaterial=False, CopyEnvironment=False, CopyShape=False)
CopySample(InputWorkspace='peaks', OutputWorkspace='TOPAZ_7421', CopyName=False, CopyMaterial=False, CopyEnvironment=False, CopyShape=False)
SelectCellOfType(PeaksWorkspace='peaks', CellType='Monoclinic', Centering='C', Apply=True, NumIndexed=34, AverageError=0.010185345069533849)
CopySample(InputWorkspace='peaks', OutputWorkspace='TOPAZ_7241_md', CopyName=False, CopyMaterial=False, CopyEnvironment=False, CopyShape=False)
CopySample(InputWorkspace='peaks', OutputWorkspace='TOPAZ_7421', CopyName=False, CopyMaterial=False, CopyEnvironment=False, CopyShape=False)
TransformHKL(PeaksWorkspace='peaks', NumIndexed=34, AverageError=0.010185345069533849)
CopySample(InputWorkspace='peaks', OutputWorkspace='TOPAZ_7241_md', CopyName=False, CopyMaterial=False, CopyEnvironment=False, CopyShape=False)
CopySample(InputWorkspace='peaks', OutputWorkspace='TOPAZ_7421', CopyName=False, CopyMaterial=False, CopyEnvironment=False, CopyShape=False)
CopySample(InputWorkspace='TOPAZ_7241_md', OutputWorkspace='TOPAZ_7421', CopyName=False, CopyMaterial=False, CopyEnvironment=False, CopyShape=False)
CropWorkspace(InputWorkspace='TOPAZ_7421', OutputWorkspace='TOPAZ_7421', XMin=100)