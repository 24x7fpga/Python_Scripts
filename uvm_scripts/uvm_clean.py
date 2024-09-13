#!/usr/bin/env python3

import os
import sys
import subprocess

home = os.environ['HOME']

path = home + "/Projects/fpgaProjects/UVM/uvm_verification/*/verif"

try:
    os.system("rm -rf "+path)
    print("Cleaned! ;)")
except:
    print("could not execute command")
