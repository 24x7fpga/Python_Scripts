#!/usr/bin/env python3

import os
import sys
import subprocess

home = os.environ['HOME']

v_path = home+ "/vivado*"

try:
    os.system("rm -f "+v_path)
    print("Cleaned! ;)")
except:
    print("could not execute command")
