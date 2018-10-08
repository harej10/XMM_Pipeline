import numpy as np
import os
import argparse
import glob

#Start in directory with just the obsid.tar.gz file


def XMMstartup(obsid):
	#Create folders and untar products
	os.system('mkdir '+obsid)
	os.chdir(obsid)
	os.system('mkdir odf')
	os.chdir('../')
	os.system('cp '+obsid+'.tar.gz '+obsid+'/odf/')
	os.chdir(obsid+'/odf/')
	os.system('gunzip '+obsid+'.tar.gz')
	os.system('tar -xvf '+obsid+'.tar')
	#os.system('rm '+obsid+'.tar')
	os.system('tar -xvf *.TAR')
	
	#Run cifbuild and odfingest
	cwd=os.getcwd()
	os.putenv("SAS_ODF", cwd)
	os.system('cifbuild')
	os.putenv("SAS_CCF", cwd + "/ccf.cif")
	os.system('odfingest')
	newodfpath = glob.glob('*SUM.SAS')
	os.putenv("SAS_ODF", cwd + '/' + newodfpath[0])
	
	#Run emproc and epproc
	os.system('emproc')
	os.system('epproc')
	
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Set up SAS evnironment and run cifbuild, odfingest, and reprocess files")
    parser.add_argument("obsid", type=str)
    args = parser.parse_args()

    XMMstartup(args.obsid)
