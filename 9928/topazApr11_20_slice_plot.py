workingdir="/SNS/users/rwp/9928/20/"

runs=range(8005,8017) 


for r in runs:
    print "************* processing run "+str(r)+" ***********************"
    LoadMD(Filename=workingdir+"TOPAZ_"+str(r)+"_MDH.nxs",OutputWorkspace="data")
    print "************* processing vanadium for run "+str(r)+" ***********************"
    LoadMD(Filename=workingdir+"VAN_"+str(r)+"_MDH.nxs",OutputWorkspace="van")
    DivideMD(LHSWorkspace="data",RHSWorkspace="van",OutputWorkspace=str(r))


for r in runs:
    plotSlice(str(r),xydim=['[H,0,0]','[0,0,L]'],slicepoint=[0,-1,0], colormax=1e-5,normalization=0)
