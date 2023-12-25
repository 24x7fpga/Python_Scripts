#!/usr/bin/env python3

import os
import sys

name = sys.argv[1]
home = os.environ['HOME']

length = len(sys.argv[1:])

# top-module path
path = home + "/Projects/fpgaProjects/iVerilog/design/"+name+"/" 

#top-module with data path
d_path  = home + "/Projects/fpgaProjects/iVerilog/design/"+name+"/"+name+".v"

# test bench path
tb_path = home + "/Projects/fpgaProjects/iVerilog/tb_design/tb_"+name+"/"

# path for module instantiation
if(length > 1):
    subd_path=[0 for i in range(length-1)]
    for i in range(length-1):
        if(os.path.isfile(path+sys.argv[2]+".v")):
            subd_path = home + "/Projects/fpgaProjects/iVerilog/design/"+sys.argv[1]+"/"+sys.argv[i+2]+".v"
            d_path = d_path +" "+subd_path
        else:
            subd_path = home + "/Projects/fpgaProjects/iVerilog/design/"+sys.argv[i+2]+"/"+sys.argv[i+2]+".v"
            d_path = d_path +" "+subd_path


os.chdir(tb_path)
print(tb_path)
print(os.getcwd())

# os.system("ls -l")

try:
    os.system("iverilog -o tb_"+name+" tb_"+name+".v "+d_path)
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
    

