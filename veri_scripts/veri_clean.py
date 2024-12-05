#!/usr/bin/env python3

import os
import sys
import subprocess

home = os.environ['HOME']

path = home + "/Projects/FPGA_Projects/RTL"

try:
    os.system("find "+path+" -type d \( -name \"obj_dir\" \) -print")
    os.system("find "+path+" -type d \( -name \"obj_dir\" \) -exec rm -r {} +")
    print("Cleaned! ;)")
except:
    print("could not execute command")
