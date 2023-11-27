#!/usr/bin/env python3

import os
import sys

name = sys.argv[1]
home = os.environ['HOME']

d_path  = home + "Projects/fpgaProjects/iVerilog/design/"+name+"/"
tb_path = home + "Projects/fpgaProjects/iVerilog/tb_design/tb_"+name+"/"

os.chdir(tb_path)
print(tb_path)
print(os.getcwd())

#os.system("ls -l")


try:
    os.system("iverilog -o "+tb_path+"tb_"+name+" "+d_path+name+".v tb_"+name+".v")
    print("iverilog command successful ;)")
    os.system("ls -l")
except:
    print("iverilog command failed ;(")


try:
    os.system("vvp "+tb_path+"tb_"+name)
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
    

