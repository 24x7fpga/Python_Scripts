#!/usr/bin/env python3

import os
import sys
import subprocess

name = sys.argv[1]
home = os.environ['HOME']

t_path = home + "/Projects/FPGA_Projects/SV/sv_tcl_script/sv_cstrs.tcl"
d_path = home + "/Projects/FPGA_Projects/SV/sv_verification/cstrs_challenges/"+name

# Check if the proj exists and overwrite
if os.path.isdir(d_path+"/verif"):
    print('----------- Project Overwite -----------')
    subprocess.run(["rm", "-rf", d_path+"/verif"], check=True)


# Create the proj folder 
os.mkdir(d_path+"/verif")

# Invoke Vivado from inside the proj folder 
os.chdir(d_path+"/verif")

vivado_command = [
    "vivado",
    "-mode", "batch",
    "-source", t_path,
    "-tclargs", name, d_path
]

subprocess.run(vivado_command)
