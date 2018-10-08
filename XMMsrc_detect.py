import os
import numpy as np
import argparse
import glob


def XMMsrc_detect(obsid):
	#Create images in different energy bands
	os.chdir(obsid+'/clean/mos1')
	os.system("evselect table=M1_noflare.fits:EVENTS imagebinning='binSize' imageset='m1_image_full.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [200:12000])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m1gti.fits,TIME)'")
	os.system("evselect table=M1_noflare.fits:EVENTS imagebinning='binSize' imageset='m1_image_b1.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [200:500])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m1gti.fits,TIME)'")
	os.system("evselect table=M1_noflare.fits:EVENTS imagebinning='binSize' imageset='m1_image_b2.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [500:1000])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m1gti.fits,TIME)'")
	os.system("evselect table=M1_noflare.fits:EVENTS imagebinning='binSize' imageset='m1_image_b3.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [1000:2000])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m1gti.fits,TIME)'")
	os.system("evselect table=M1_noflare.fits:EVENTS imagebinning='binSize' imageset='m1_image_b4.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [2000:4500])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m1gti.fits,TIME)'")
	os.system("evselect table=M1_noflare.fits:EVENTS imagebinning='binSize' imageset='m1_image_b5.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [4500:12000])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m1gti.fits,TIME)'")


	os.chdir('../mos2')
	os.system("evselect table=M2_noflare.fits:EVENTS imagebinning='binSize' imageset='m2_image_full.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [200:12000])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m2gti.fits,TIME)'")
	os.system("evselect table=M2_noflare.fits:EVENTS imagebinning='binSize' imageset='m2_image_b1.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [200:500])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m2gti.fits,TIME)'")
	os.system("evselect table=M2_noflare.fits:EVENTS imagebinning='binSize' imageset='m2_image_b2.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [500:1000])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m2gti.fits,TIME)'")
	os.system("evselect table=M2_noflare.fits:EVENTS imagebinning='binSize' imageset='m2_image_b3.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [1000:2000])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m2gti.fits,TIME)'")
	os.system("evselect table=M2_noflare.fits:EVENTS imagebinning='binSize' imageset='m2_image_b4.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [2000:4500])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m2gti.fits,TIME)'")
	os.system("evselect table=M2_noflare.fits:EVENTS imagebinning='binSize' imageset='m2_image_b5.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM&&(PI in [4500:12000])&&(PATTERN in [0:12])&&(FLAG==0) && gti(m2gti.fits,TIME)'")

	os.chdir('../pn')
	os.system("evselect table=PN_noflare.fits:EVENTS imagebinning='binSize' imageset='pn_image_full.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EP&&(PI in [300:12000])&&(PATTERN in [0:4])&&(FLAG==0) && gti(pngti.fits,TIME)'")
	os.system("evselect table=PN_noflare.fits:EVENTS imagebinning='binSize' imageset='pn_image_b1.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EP&&(PI in [300:500])&&(PATTERN in [0:4])&&(FLAG==0) && gti(pngti.fits,TIME)'")
	os.system("evselect table=PN_noflare.fits:EVENTS imagebinning='binSize' imageset='pn_image_b2.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EP&&(PI in [500:1000])&&(PATTERN in [0:4])&&(FLAG==0) && gti(pngti.fits,TIME)'")
	os.system("evselect table=PN_noflare.fits:EVENTS imagebinning='binSize' imageset='pn_image_b3.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EP&&(PI in [1000:2000])&&(PATTERN in [0:4])&&(FLAG==0) && gti(pngti.fits,TIME)'")
	os.system("evselect table=PN_noflare.fits:EVENTS imagebinning='binSize' imageset='pn_image_b4.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EP&&(PI in [2000:4500])&&(PATTERN in [0:4])&&(FLAG==0) && gti(pngti.fits,TIME)'")
	os.system("evselect table=PN_noflare.fits:EVENTS imagebinning='binSize' imageset='pn_image_b5.fits' withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EP&&(PI in [4500:12000])&&(PATTERN in [0:4])&&(FLAG==0) && gti(pngti.fits,TIME)'")

	#Make new directory to house source detection files
	os.chdir('../')
	os.system('mkdir src_det')
	os.chdir('mos1')
	os.system('cp *m1_image* ../src_det')
	os.chdir('../mos2')
	os.system('cp *m2_image* ../src_det')
	os.chdir('../pn')
	os.system('cp *pn_image* ../src_det')
	os.chdir('../src_det')
	
	#Run Source detection NOTE THE CURRENT ECFs ARE FOR THIN FILTER
	os.chdir('../../odf')
	cwd=os.getcwd()
	os.putenv("SAS_CCF", cwd + "/ccf.cif")
	newodfpath = glob.glob('*SUM.SAS')
	os.putenv("SAS_ODF", cwd + '/' + newodfpath[0])
	os.system('cp *AttHk.ds* ../clean/src_det')
	os.chdir('../clean/src_det')
	attfile=glob.glob('*AttHk.ds*')
	os.system('edetect_chain imagesets=""m1_image_b1.fits" "m1_image_b2.fits" "m1_image_b3.fits" "m1_image_b4.fits" "m1_image_b5.fits" "m2_image_b1.fits" "m2_image_b2.fits" "m2_image_b3.fits" "m2_image_b4.fits" "m2_image_b5.fits" "pn_image_b1.fits" "pn_image_b2.fits" "pn_image_b3.fits" "pn_image_b4.fits" "pn_image_b5.fits"" eventsets="../mos1/M1_noflare.fits ../mos2/M2_noflare.fits ../pn/PN_noflare.fits" attitudeset='+attfile[0]+' pimin="200 500 1000 2000 4500 200 500 1000 2000 4500 200 500 1000 2000 4500" pimax="500 1000 2000 4500 12000 500 1000 2000 4500 12000 500 1000 2000 4500 12000" ecf="1.734 1.746 2.041 0.737 0.145 0.991 1.387 1.789 0.703 0.150 9.525 8.121 5.867 1.953 0.578" eboxl_list="all_eboxlist_l.fits" eboxm_list="all_eboxlist_m.fits" esp_nsplinenodes=16 eml_list="all_emllist.fits" esen_mlmin=15')
	os.system("emosaic imagesets='m1_image_full.fits m2_image_full.fits pn_image_full.fits' mosaicedset=mosaic.ds")




if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Make EPIC images and detect sources in them.")
    parser.add_argument("obsid", type=str)
    args = parser.parse_args()

    XMMsrc_detect(args.obsid)
