#!/usr/bin/env python3

import os
import sys
import subprocess

name = sys.argv[1]
home = os.environ['HOME']

t_path = home + "/Projects/FPGA_Projects/RTL/rtl_tcl_scripts/rtl_run.tcl"
d_path = home + "/Projects/FPGA_Projects/RTL/rtl_designs/"+name

# Check if the proj exists and overwrite
if os.path.isdir(d_path+"/proj"):
    print('----------- Project Overwite -----------')
    subprocess.run(["rm", "-rf", d_path+"/proj"], check=True)


# Create the proj folder 
os.mkdir(d_path+"/proj")

# Invoke Vivado from inside the proj folder 
os.chdir(d_path+"/proj")

vivado_command = [
    "vivado",
    "-mode", "batch",
    "-source", t_path,
    "-tclargs", name, d_path
]

subprocess.run(vivado_command)
