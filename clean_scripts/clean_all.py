#!/usr/bin/env python3

import os
import sys
import subprocess

home = os.environ['HOME']

uvm_path = home + "/Projects/FPGA_Projects/UVM/uvm_verification/"
rtl_path = home + "/Projects/FPGA_Projects/RTL"
sv_path  = home + "/Projects/FPGA_Projects/SV/sv_verification/"
v_log    = home + "/Projects/FPGA_Projects/RTL/"
v_path   = home+ "/vivado*"

try:
    # iVerilog
    os.system("find "+rtl_path+" -type f \( -name \"*.vvp\" -o -name \"*.vcd\" \) -print")
    os.system("find "+rtl_path+" -type f \( -name \"*.vvp\" -o -name \"*.vcd\" \) -exec rm -r {} +")
    # Verilator
    os.system("find "+rtl_path+" -type d \( -name \"obj_dir\" \) -print")
    os.system("find "+rtl_path+" -type d \( -name \"obj_dir\" \) -exec rm -r {} +")
    # SV
    os.system("find "+sv_path+" -type d -name \"verif\" -print")
    os.system("find "+sv_path+" -type d -name \"verif\" -exec rm -r {} +")
    # UVM
    os.system("find "+uvm_path+" -type d -name \"verif\" -print")
    os.system("find "+uvm_path+" -type d -name \"verif\" -exec rm -r {} +")
    # Vivado Log Files
    os.system("rm -d "+v_log+".Xil")
    os.system("rm -f "+v_log+"vivado*")
    os.system("rm -f "+v_path)
    print("Cleaned! ;)")
except:
    print("could not execute command")
