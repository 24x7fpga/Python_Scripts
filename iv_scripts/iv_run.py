#!/usr/bin/env python3

import os
import sys
import glob 

name = sys.argv[1]
home = os.environ['HOME']

length = len(sys.argv[1:])

# Design path
path = home + "/Projects/FPGA_Projects/RTL/design/"+name+"/" 

# move to design directory
os.chdir(path)
#print(path)
#print(os.getcwd())
#os.system("ls -l")

# Add all the files
all_tb_files = os.listdir(path)
files = [file for file in all_tb_files if ".sv" in file or ".svh" in file]
files = " ".join(files)

# Run iVerilog
try:
    os.system("iverilog -g2012 -o tb_"+name+".vvp "+files)
    print("iverilog command successful ;)")
    os.system("ls -l")
except:
    print("iverilog command failed ;(")

try:
    os.system("vvp tb_"+name+".vvp")
    print("vvp command successful ;)")
except:
    print("vvp command failed ;(")

# Open GTKWave
try:
    os.system("gtkwave tb_"+name+".vcd")
    print("gtwave command successful ;)")
except:
    print("gtwave command failed ;(")
    

