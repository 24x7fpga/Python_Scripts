#!/usr/bin/env python3

import os
import sys
import subprocess

name = sys.argv[1]
home = os.environ['HOME']

t_path = home + "/Projects/FPGA_Projects/UVM/uvm_tcl_script/uvm_run.tcl"
d_path = home + "/Projects/FPGA_Projects/UVM/uvm_verification/"+name


vivado_command = [
    "vivado",
    "-mode", "batch",
    "-source", t_path,
    "-tclargs", name, d_path
]

subprocess.run(vivado_command)
