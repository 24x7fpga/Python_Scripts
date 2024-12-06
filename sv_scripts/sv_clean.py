#!/usr/bin/env python3

import os
import sys
import subprocess

home = os.environ['HOME']

path = home + "/Projects/FPGA_Projects/SV/sv_verification/"

try:
    os.system("find "+path+" -type d -name \"verif\" -exec rm -r {} +")
    print("Cleaned! ;)")
except:
    print("could not execute command")
