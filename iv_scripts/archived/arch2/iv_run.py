#!/usr/bin/env python3

import os
import sys
import glob 


name = sys.argv[1]
home = os.environ['HOME']

length = len(sys.argv[1:])

# top-module path
path = home + "/Projects/FPGA_Projects/RTL/design/"+name+"/" 

# check file extension
#if(glob.glob(path+name+".v")):
#    print("Verilog File")
#    ext = ".v"
#else:
#    print("SystemVerilog File")
#    ext = ".sv"

#print(ext)
#top-module with data path
d_path  = home + "/Projects/FPGA_Projects/RTL/design/"+name+"/"
# test bench path
tb_path = home + "/Projects/FPGA_Projects/RTL/design/"+name+"/"

# path for module instantiation
if(length > 1):
    subd_path=[0 for i in range(length-1)]
    for i in range(length-1):
        if(os.path.isfile(path+sys.argv[2]+ext)):
            subd_path = home + "/Projects/FPGA_Projects/RTL/design/"+sys.argv[1]+"/"+sys.argv[i+2]+ext
            d_path = d_path +" "+subd_path
        else:
            subd_path = home + "/Projects/FPGA_Projects/RTL/design/"+sys.argv[i+2]+"/"+sys.argv[i+2]+ext
            d_path = d_path +" "+subd_path





all_d_files = os.listdir(path)
d_files = [file for file in all_d_files if ".sv" in file or ".svh" in file]
print(d_files)

for i in range(len(d_files)):
    subd_path = path + d_files[i] 
    d_path = d_path +" "+subd_path  

all_tb_files = os.listdir(tb_path)
tb_files = [file for file in all_tb_files if ".sv" in file or ".svh" in file]
tb_files = " ".join(tb_files)
#print(tb_files)

all_tb_files = os.listdir(path)
files = [file for file in all_tb_files if ".sv" in file or ".svh" in file]
files = " ".join(files)
#############################
# os.system("ls -l")

# move to testbench directory
os.chdir(tb_path)
print(tb_path)
print(os.getcwd())

try:
    #os.system("iverilog -g2012 -o tb_"+name+".vvp "+tb_files+" "+d_path)
    os.system("iverilog -g2012 -o tb_"+name+".vvp "+files)
    print("iverilog -g2012 -o tb_"+name+".vvp "+files)
    #print("iverilog -g2012 -o tb_"+name+".vvp "+tb_path+tb_files+" "+d_path)
    print("iverilog command successful ;)")
    os.system("ls -l")
except:
    print("iverilog command failed ;(")


try:
    os.system("vvp "+tb_path+"tb_"+name+".vvp")
    os.system("ls -l")
    print("vvp command successful ;)")
except:
    print("vvp command failed ;(")
        

try:
    os.system("ls")
except:
    print(" could not execute command")

try:
    os.system("gtkwave tb_"+name+".vcd")
    print("gtwave command successful ;)")
except:
    print("gtwave command failed ;(")
    

