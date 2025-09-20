#!/usr/bin/env python3

import os
import sys
import subprocess

home = os.environ['HOME']

path = home + "/Projects/FPGA_Projects/RTL"

try:
    os.system("find "+path+" -type f \\( -name \"*.vvp\" -o -name \"*.vcd\" \\) -print")
    os.system("find "+path+" -type f \\( -name \"*.vvp\" -o -name \"*.vcd\" \\) -exec rm -r {} +")
    print("Cleaned! ;)")
except:
    print("could not execute command")
