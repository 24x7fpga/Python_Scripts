#!/usr/bin/env python3

import os
import sys

name = sys.argv[1]
home = os.environ['HOME']

proj_path  = home + "/Projects/FPGA_Projects/RTL/rtl_designs"
temp_path  = home + "/Projects/FPGA_Projects/RTL/rtl_templates"

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
	    
	# rename design and top module 
	try:
	    os.chdir(proj_path+"/"+name)  
	    os.system("mv design.sv "+name+".sv")  
	    os.system("mv tb_design.sv tb_"+name+".sv")
	    print('Design Rename Successful ;)')
	except:
	    print('Design Rename Failed ;(')

	# rename the design files
	try:
	    os.chdir(proj_path+"/"+name)  
	    os.system("sed -i 's/$ARG/"+name+"/g' "+name+".sv")
	    os.system("sed -i 's/$ARG/"+name+"/g' tb_"+name+".sv")  
	    os.system("sed -i 's/$ARG/"+name+"/g' interface.sv")
	    print('Renamed the Designed Files  ;)')
	except:
	    print('Renaming Failed ;(')
