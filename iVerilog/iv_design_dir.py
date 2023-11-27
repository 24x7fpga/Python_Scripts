#!/usr/bin/env python3

import os
import sys

name = sys.argv[1]
home = os.environ['HOME']
path = 'Projects/fpgaProjects/iVerilog'

newdir = home+path

try:
    os.chdir(newdir+'/design')
    os.mkdir(name)
    os.chdir(newdir+'/tb_design')
    os.mkdir("tb_"+name)
    print('Directory creation successful ;)')
except:
    print('Directory creation Failed ;(')

