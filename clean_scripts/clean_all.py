#!/usr/bin/env python3

import os
import sys
import subprocess

home = os.environ['HOME']

uvm_path = home + "/Projects/FPGA_Projects/UVM/uvm_verification/"
rtl_path = home + "/Projects/FPGA_Projects/RTL"
sv_path  = home + "/Projects/FPGA_Projects/SV/sv_verification/"
v_log    = home + "/Projects/FPGA_Projects/RTL/rtl_designs/"


try:
    # iVerilog
    os.system("find "+rtl_path+" -type f \\( -name \"*.vvp\" -o -name \"*.vcd\" \\) -print")
    os.system("find "+rtl_path+" -type f \\( -name \"*.vvp\" -o -name \"*.vcd\" \\) -exec rm -r {} +")
    # Verilator
    os.system("find "+rtl_path+" -type d \\( -name \"obj_dir\" \\) -print")
    os.system("find "+rtl_path+" -type d \\( -name \"obj_dir\" \\) -exec rm -r {} +")
    # SV
    os.system("find "+sv_path+" -type d -name \"verif\" -print")
    os.system("find "+sv_path+" -type d -name \"verif\" -exec rm -r {} +")
    # UVM
    os.system("find "+uvm_path+" -type d -name \"verif\" -print")
    os.system("find "+uvm_path+" -type d -name \"verif\" -exec rm -r {} +")
    # Vivado 
    os.system("find "+v_log+" -type d -name \"proj\" -print")
    os.system("find "+v_log+" -type d -name \"proj\" -exec rm -r {} +")
    
    print("Cleaned! ;)")
except:
    print("could not execute command")
