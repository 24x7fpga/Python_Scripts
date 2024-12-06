#!/usr/bin/env python3

import os
import sys

name = sys.argv[1]
home = os.environ['HOME']

proj_path  = home + "/Projects/FPGA_Projects/SV/sv_verification/cstrs_challenges"
temp_path  = home + "/Projects/FPGA_Projects/SV/sv_templates/constraints"

#check if the folder already exists
if name in os.listdir(proj_path):
    	print('----------- WARNING -----------')
    	print('   folder name already exists   ')
else:
	# create a folder is the project name
	try:
	    os.chdir(proj_path)
	    os.mkdir(name)
	    print('Directory creation successful ;)')
	except:
	    print('Directory creation Failed ;(')

	# copy the template file into the source directory
	try:    
	    os.system("cp -f "+temp_path+"/* "+proj_path+"/"+name)
	    print('Copied the Template Files ;)')
	except:
	    print('Copying Templates Failed ;(')
	    
	# rename top module 
	try:
	    os.chdir(proj_path+"/"+name)    
	    os.system("mv tb.sv tb_"+name+".sv")
	    print('Topmodule Rename Successful ;)')
	except:
	    print('Topmodule Rename Failed ;(')

	# rename the test program
	try:
	    os.chdir(proj_path+"/"+name)    
	    os.system("sed -i 's/$ARG/"+name+"/g' tb_"+name+".sv")
	    print('Renamed the Program ;)')
	except:
	    print('Renaming the Program Failed ;(')
	    
    
