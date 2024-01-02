#!/usr/bin/env python3

import os
import sys

name = sys.argv[1]
home = os.environ['HOME']

d_path  = home + "/Projects/fpgaProjects/iVerilog/design"
tb_path = home + "/Projects/fpgaProjects/iVerilog/tb_design"


# create design and test-bench folders
try:
    os.chdir(d_path)
    os.mkdir(name)
    os.chdir(tb_path)
    os.mkdir("tb_"+name)
    print('Directory creation successful ;)')
except:
    print('Directory creation Failed ;(')

# create design files
try:
    nw_d=d_path+"/"+name+"/"
    os.chdir(nw_d)
    f_d=open(name+".v","x")
    print('Design File Created ;)')
   
    # timescale
    scale = ["`timescale 1ns/1ns \n"] 
    print('Timescale ;)')

    # write Design module, clock and resets
    module = ["module "+name+ "(/*AUTOARG*/); \n",
		    "input clk; \n",
	        "input rst; \n"]
    print('Module Written ;)')

    # auto wire and register 
    rc = ["/*AUTOREG*/ \n",
		 "/*AUTOWIRE*/ \n"]
    print('Auto WIRE and REG ;)')

    # DUT instantiation
    init = ["<module> MOD1 (/*AUTOINST*/); \n"]
    print('Module Instantiation ;)')

    # endmodule
    end = ["endmodule \n"]
    print('EndModule ;)')

    # locate the design file
    loc = ["// Local Variables: \n",
              "// verilog-library-directories:(\"~/Projects/fpgaProjects/iVerilog/design/*\") \n",
	      "// End:"]
    print('Emac linkers ;)')

    # write all the lines to a single list
    content = scale + module + rc + init + end + loc
    print('Files content Stitched ;)')

    # write to the file
    f_d.writelines(content)
    print('Design file written ;)')

    # close the file
    f_d.close()
    print('File Closed ;)')
except:
    print('Design File Creation Failed ;( ')
    
 # create test-bench files
try:
    nw_tb=tb_path+"/tb_"+name+"/"
    os.chdir(nw_tb)
    f_tb=open("tb_"+name+".v","x")
    print('Test-Bench File Created ;)')

    # timescale
    scale = ["`timescale 1ns/1ns \n"] 
    print('Timescale ;)')

    # write test-bench module
    tb_module = ["module tb_"+name+ "(); \n",
		 "/*AUTOREG*/ \n",
		 "/*AUTOWIRE*/ \n"]
    print('Module Written ;)')

    # clock and reset
    tb_rc = ["reg clk; \n",
	     "reg rst; \n"]
    print('Clocks and Resets ;)')

    # DUT instantiation
    tb_init = [name+ " DUT (/*AUTOINST*/); \n"]
    print('Design Module Instantiated ;)')

    # creat clock
    tb_clk = ["initial clk = 0; \n" ,"always #5 clk = ~clk; \n"]
    print('Clocks and Reset Initialized ;)')

    # dump file
    tb_dump = ["initial begin \n",
	       "$dumpfile(\"tb_"+name+".vcd\"); \n",
	       "$dumpvars(0,tb_"+name+"); \n",
	       "end \n"]
    print('.vcd Dump ;)')

    # endmodule
    tb_end = ["endmodule \n"]
    print('EndModule ;)')

    # locate the design file
    tb_loc = ["// Local Variables: \n",
              "// verilog-library-directories:(\"~/Projects/fpgaProjects/iVerilog/design/*\") \n",
	      "// End:"]
    print('Emac linkers ;)')

    # write all the lines to a single list
    tb_content = scale + tb_module + tb_rc + tb_init + tb_clk + tb_dump + tb_end + tb_loc
    print('Files content Stitched ;)')

    # write to the file
    f_tb.writelines(tb_content)
    print('Test-bench file written ;)')

    # close the file
    f_tb.close()
    print('File Closed ;)')
except:
    print('Test-Bench File Creation Failed ;( ')
    

# open emacs
#try:
#    os.system("emacs tb_"+name+".v")
#    print("Test-bench successful ;)")
#except:
#    print("Test-bench failure ;(")



