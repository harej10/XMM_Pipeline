import os
import numpy as np
import argparse
import glob

def XMMspec_ext(obsid,srcid,srcx,srcy,srcrad,bkgx,bkgy,bkgrad):
	os.chdir(obsid+'/odf')
	cwd=os.getcwd()
	os.putenv("SAS_CCF", cwd + "/ccf.cif")
	newodfpath = glob.glob('*SUM.SAS')
	os.putenv("SAS_ODF", cwd + '/' + newodfpath[0])
	os.chdir('../clean/mos1')
	os.system("evselect table=M1_noflare.fits withspectrumset=yes spectrumset=M1source"+srcid+"_spectrum.fits energycolumn=PI spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999 expression='#XMMEA_EM && (PATTERN<=12) && ((X,Y) IN circle("+srcx+","+srcy+","+srcrad+"))'")
	os.system("evselect table=M1_noflare.fits withspectrumset=yes spectrumset=M1bkg"+srcid+"_spectrum.fits energycolumn=PI spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999 expression='#XMMEA_EM && (PATTERN<=12) && ((X,Y) IN circle("+bkgx+","+bkgy+","+bkgrad+"))'")
	os.system('backscale spectrumset=M1source'+srcid+'_spectrum.fits badpixlocation=M1_noflare.fits')
	os.system('backscale spectrumset=M1bkg'+srcid+'_spectrum.fits badpixlocation=M1_noflare.fits')
	os.system('rmfgen spectrumset=M1source'+srcid+'_spectrum.fits rmfset=m1'+srcid+'.rmf')
	os.system('arfgen spectrumset=M1source'+srcid+'_spectrum.fits arfset=m1'+srcid+'.arf withrmfset=yes rmfset=m1'+srcid+'.rmf badpixlocation=M1_noflare.fits detmaptype=psf')
	os.system('specgroup spectrumset=M1source'+srcid+'_spectrum.fits mincounts=1 rmfset=m1'+srcid+'.rmf arfset=m1'+srcid+'.arf backgndset=M1bkg'+srcid+'_spectrum.fits groupedset=M1_src'+srcid+'_spectrum_grp1.fits')
	
	
	os.chdir('../mos2')
	os.system("evselect table=M2_noflare.fits withspectrumset=yes spectrumset=M2source"+srcid+"_spectrum.fits energycolumn=PI spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999 expression='#XMMEA_EM && (PATTERN<=12) && ((X,Y) IN circle("+srcx+","+srcy+","+srcrad+"))'")
	os.system("evselect table=M2_noflare.fits withspectrumset=yes spectrumset=M2bkg"+srcid+"_spectrum.fits energycolumn=PI spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999 expression='#XMMEA_EM && (PATTERN<=12) && ((X,Y) IN circle("+bkgx+","+bkgy+","+bkgrad+"))'")
	os.system('backscale spectrumset=M2source'+srcid+'_spectrum.fits badpixlocation=M2_noflare.fits')
	os.system('backscale spectrumset=M2bkg'+srcid+'_spectrum.fits badpixlocation=M2_noflare.fits')
	os.system('rmfgen spectrumset=M2source'+srcid+'_spectrum.fits rmfset=m2'+srcid+'.rmf')
	os.system('arfgen spectrumset=M2source'+srcid+'_spectrum.fits arfset=m2'+srcid+'.arf withrmfset=yes rmfset=m2'+srcid+'.rmf badpixlocation=M2_noflare.fits detmaptype=psf')
	os.system('specgroup spectrumset=M2source'+srcid+'_spectrum.fits mincounts=1 rmfset=m2'+srcid+'.rmf arfset=m2'+srcid+'.arf backgndset=M2bkg'+srcid+'_spectrum.fits groupedset=M2_src'+srcid+'_spectrum_grp1.fits')
	
	os.chdir('../pn')
	os.system("evselect table=PN_noflare.fits withspectrumset=yes spectrumset=PNsource"+srcid+"_spectrum.fits energycolumn=PI spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479 expression='(FLAG==0) && (PATTERN<=4) && ((X,Y) IN circle("+srcx+","+srcy+","+srcrad+"))'")
	os.system("evselect table=PN_noflare.fits withspectrumset=yes spectrumset=PNbkg"+srcid+"_spectrum.fits energycolumn=PI spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479 expression='(FLAG==0) && (PATTERN<=4) && ((X,Y) IN circle("+bkgx+","+bkgy+","+bkgrad+"))'")
	os.system('backscale spectrumset=PNsource'+srcid+'_spectrum.fits badpixlocation=PN_noflare.fits')
	os.system('backscale spectrumset=PNbkg'+srcid+'_spectrum.fits badpixlocation=PN_noflare.fits')
	os.system('rmfgen spectrumset=PNsource'+srcid+'_spectrum.fits rmfset=PN'+srcid+'.rmf')
	os.system('arfgen spectrumset=PNsource'+srcid+'_spectrum.fits arfset=PN'+srcid+'.arf withrmfset=yes rmfset=PN'+srcid+'.rmf badpixlocation=PN_noflare.fits detmaptype=psf')
	os.system('specgroup spectrumset=PNsource'+srcid+'_spectrum.fits mincounts=1 rmfset=PN'+srcid+'.rmf arfset=PN'+srcid+'.arf backgndset=PNbkg'+srcid+'_spectrum.fits groupedset=PN_src'+srcid+'_spectrum_grp1.fits')
	
	
	
	
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Extract a spectrum for a given source position and background in detector units")
    parser.add_argument("obsid", type=str)
    parser.add_argument("srcid", type=str)
    parser.add_argument("srcx", type=str)
    parser.add_argument("srcy", type=str)
    parser.add_argument("srcrad", type=str)
    parser.add_argument("bkgx", type=str)
    parser.add_argument("bkgy", type=str)
    parser.add_argument("bkgrad", type=str)
    args = parser.parse_args()
    
    XMMspec_ext(args.obsid,args.srcid,args.srcx,args.srcy,args.srcrad, args.bkgx, args.bkgy, args.bkgrad)
