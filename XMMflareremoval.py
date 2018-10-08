import os
import numpy as np
import argparse
import glob


def XMMflareremoval(obsid,ratem12,ratepn):
	#Prepare directories for cleaned products
	os.chdir(obsid +'/')
	os.system('mkdir clean')
	os.chdir('clean')
	os.system('mkdir mos1')
	os.system('mkdir mos2')
	os.system('mkdir pn')
	os.chdir('../odf/')
	
	#Run filtering on each detector
	evtfiles=glob.glob('*Imaging*')
	m1filter = "'#XMMEA_EM && (PI>10000) && (PATTERN==0)'"
	os.system('evselect table=' + evtfiles[0] + ' withrateset=Y rateset=rateM1.fits maketimecolumn=Y timebinsize=100 makeratecolumn=Y expression='+m1filter)
	#os.system('dsplot table=rateM1.fits x=TIME y=RATE')

	#Run filtering on each detector
	evtfiles=glob.glob('*Imaging*')
	m2filter = "'#XMMEA_EM && (PI>10000) && (PATTERN==0)'"
	os.system('evselect table=' + evtfiles[1] + ' withrateset=Y rateset=rateM2.fits maketimecolumn=Y timebinsize=100 makeratecolumn=Y expression='+m2filter)
	#os.system('dsplot table=rateM2.fits x=TIME y=RATE')

	#Run filtering on each detector
	evtfiles=glob.glob('*Imaging*')
	pnfilter = "'#XMMEA_EP && (PI>10000&&PI<12000) && (PATTERN==0)'"
	os.system('evselect table=' + evtfiles[2] + ' withrateset=Y rateset=ratePN.fits maketimecolumn=Y timebinsize=100 makeratecolumn=Y expression='+pnfilter)
	#os.system('dsplot table=ratepn.fits x=TIME y=RATE')
	
	#Filter time intervals for high particle background
	m1gtifilter="'RATE<="+ratem12+"' gtiset=EPICgti.fits"
	os.system('tabgtigen table=rateM1.fits expression='+m1gtifilter+' gtiset=m1gti.fits')
	m2gtifilter="'RATE<="+ratem12+"' gtiset=EPICgti.fits"
	os.system('tabgtigen table=rateM2.fits expression='+m1gtifilter+' gtiset=m2gti.fits')
	pngtifilter="'RATE<="+ratepn+"' gtiset=EPICgti.fits"
	os.system('tabgtigen table=ratePN.fits expression='+pngtifilter+' gtiset=pngti.fits')
	
	#Filter events for high particle background
	m1evtfilter = "'#XMMEA_EM && gti(m1gti.fits,TIME) && (PI>150)'"
	os.system('evselect table='+evtfiles[0]+' withfilteredset=Y filteredset=M1_noflare.fits destruct=Y keepfilteroutput=T expression='+m1evtfilter)
	m2evtfilter = "'#XMMEA_EM && gti(m2gti.fits,TIME) && (PI>150)'"
	os.system('evselect table='+evtfiles[1]+' withfilteredset=Y filteredset=M2_noflare.fits destruct=Y keepfilteroutput=T expression='+m2evtfilter)
	pnevtfilter = "'#XMMEA_EP && gti(pngti.fits,TIME) && (PI>150)'"
	os.system('evselect table='+evtfiles[2]+' withfilteredset=Y filteredset=PN_noflare.fits destruct=Y keepfilteroutput=T expression='+pnevtfilter)
	
	#Move files to respective directories
	os.system('mv rateM1.fits ../clean/mos1')
	os.system('mv rateM2.fits ../clean/mos2')
	os.system('mv ratePN.fits ../clean/pn')
	
	os.system('mv m1gti.fits ../clean/mos1')
	os.system('mv m2gti.fits ../clean/mos2')
	os.system('mv pngti.fits ../clean/pn')
	
	os.system('mv M1_noflare.fits ../clean/mos1')
	os.system('mv M2_noflare.fits ../clean/mos2')
	os.system('mv PN_noflare.fits ../clean/pn')		



if __name__ == '__main__':
    
	parser = argparse.ArgumentParser(description="Remove times with high flaring particle background")
	parser.add_argument("obsid", type=str)
	parser.add_argument("ratem12", type=str)
	parser.add_argument("ratepn", type=str)
	args = parser.parse_args()

	XMMflareremoval(args.obsid,args.ratem12,args.ratepn)
