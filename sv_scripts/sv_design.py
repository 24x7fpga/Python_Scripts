#!/usr/bin/env python3

import os
import sys

name = sys.argv[1]
home = os.environ['HOME']

d_path  = home + "/Projects/fpgaProjects/SystemVerilog_Verification/sv_verification"

# create design and test-bench folders
try:
    os.chdir(d_path)
    os.mkdir(name)
    print('Directory creation successful ;)')
except:
    print('Directory creation Failed ;(')

# create design files
try:
    nw_d=d_path+"/"+name+"/"
    os.chdir(nw_d)
    f_d=open("tb_"+name+".sv","x")
    print('Design File Created ;)')
   
    # write Design module, clock and resets
    module = ["module tb_"+name+"; \n"]
    print('Module Written ;)')

    # auto wire and register 
    rc = ["  /*AUTOREG*/ \n",
	  "  /*AUTOWIRE*/ \n"]
    print('Auto WIRE and REG ;)')

    # endmodule
    end = ["endmodule \n"]
    print('EndModule ;)')

    # locate the design file
    loc = ["// Local Variables: \n",
           "// verilog-library-directories:(\"~/Projects/fpgaProjects/SystemVerilog_Verification/sv_verification/"+name+"/*\") \n",
	   "// End:"]
    print('Emac linkers ;)')

    # add a lines
    line = [" \n"]

    # write all the lines to a single list
    content = module + line + rc + line + line + end + loc
    print('Files content Stitched ;)')

    # write to the file
    f_d.writelines(content)
    print('Design file written ;)')

    # close the file
    f_d.close()
    print('File Closed ;)')
except:
    print('Design File Creation Failed ;( ')
    

    




