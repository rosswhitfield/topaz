#/usr/bin/python
import sys
sys.path.append("/opt/Mantid/bin")
from mantid.simpleapi import *
Load(Filename='TOPAZ_6663', OutputWorkspace='rawVan', LoaderName='LoadEventNexus', LoaderVersion='1')
ConvertUnits(InputWorkspace='rawVan', OutputWorkspace='rawVan', Target='Momentum')
CropWorkspace(InputWorkspace='rawVan', OutputWorkspace='rawVan', XMin='1.8400000000000001', XMax='10')
Rebin(InputWorkspace='rawVan', OutputWorkspace='rawVanSpectrum', Params='1.84,0.005,10', PreserveEvents='0')
Rebin(InputWorkspace='rawVan', OutputWorkspace='rawVanInt', Params='1.84,10,10', PreserveEvents='0')
SmoothNeighbours(InputWorkspace='rawVanSpectrum', OutputWorkspace='rawVanSpectrum', SumPixelsX='256', SumPixelsY='256', ZeroEdgePixels='4', ExpandSumAllPixels='1')
Multiply(LHSWorkspace='rawVanSpectrum', RHSWorkspace='rawVanInt', OutputWorkspace='test')
SaveNexus(Filename='/SNS/users/rwp/Li2-xNaxIrO4/rawVan.nxs',InputWorkspace='test')
