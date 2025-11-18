#!/usr/bin/env python3

import os
import sys
import glob 

name = sys.argv[1]
home = os.environ['HOME']

length = len(sys.argv[1:])

# Design path
path = home + "/Projects/FPGA_Projects/RTL/rtl_designs/"+name+"/" 

# move to design directory
os.chdir(path)
#print(path)
#print(os.getcwd())
#os.system("ls -l")

# Add all the files
all_tb_files = os.listdir(path)
files = [file for file in all_tb_files if ".sv" in file or ".svh" in file]
files = " ".join(files)

# Verilator Config Path
config = home + "/Projects/Python_Scripts/veri_scripts/config.vlt" 

# Remove Obj dir if exists
if os.path.isdir("obj_dir"):
    # Remove directory
    os.system("rm -rf "+path+"/obj_dir")
    # print("Obj_dir Overwritten")

# Remove .vcd if exists
if os.path.exists("tb_"+name+".vcd"):
    os.system("rm -f tb_"+name+".vcd")
    # print("VCD Overwritten")

# Run Verilator
try:
    print("Verilator Running . . .")
    os.system("verilator --trace --binary "+files+" --top tb_"+name+" "+config+" | grep -E '%(warning|error)' > /dev/null")
    print("Verilator successful ;)")
    os.system("ls -l")
except:
    print("Verilator failed ;(")

try:
    os.system("./obj_dir/Vtb_"+name)
    print("vvp command successful ;)")
except:
    print("vvp command failed ;(")

# Open GTKWave if .vcd exists
if os.path.exists("tb_"+name+".vcd"):
    os.system("gtkwave tb_"+name+".vcd")
    print("gtwave command successful ;)")
