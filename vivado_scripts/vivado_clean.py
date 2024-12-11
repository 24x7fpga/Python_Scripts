#!/usr/bin/env python3

import os
import sys
import subprocess

home   = os.environ['HOME']

path   = home + "/Projects/FPGA_Projects/RTL/rtl_designs/"

v_path = home+ "/vivado*"

try:
    os.system("find "+path+" -type d -name \"proj\" -exec rm -r {} +")
    os.system("rm -f "+v_path)
    print("Cleaned! ;)")
except:
    print("could not execute command")
