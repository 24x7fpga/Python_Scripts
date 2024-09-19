#!/usr/bin/env python3

import os
import sys
import subprocess

home = os.environ['HOME']

path = home + "/Projects/fpgaProjects/UVM/uvm_verification/*/verif"

v_path = home+ "/vivado*"

try:
    os.system("rm -rf "+path)
    os.system("rm -f "+v_path)
    print("Cleaned! ;)")
except:
    print("could not execute command")
