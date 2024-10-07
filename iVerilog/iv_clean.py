#!/usr/bin/env python3

import os
import sys
import subprocess

home = os.environ['HOME']

path = home + "/Projects/FPGA_Projects/iVerilog"


try:
    os.system("rm -rf "+path+"/*/*/*.vvp")
    os.system("rm -rf "+path+"/*/*/*.vcd")
    print("Cleaned! ;)")
except:
    print("could not execute command")
