#!/usr/bin/env python3

import os
import sys

name = sys.argv[1]
home = os.environ['HOME']
path = "Projects/fpgaProjects/iVerilog/tb_design/tb_"+name

newdir = home + path
os.chdir(newdir)
print(os.getcwd())


#open the file in write mode
file = open("tb_"+name+".v", "w")

#write test-bench module
tb_module = ["module tb_"+name+ "(); \n",
             "/*AUTOREG*/ \n",
             "/*AUTOWIRE*/ \n"]

#clock and reset
tb_rc = ["reg clk; \n",
         "reg rst; \n"]

#DUT instantiation
tb_init = [name+ " DUT (/*AUTOINST*/); \n"]

#creat clock
tb_clk = ["initial clk = 0; \n" ,"always #5 clk = ~clk; \n"]

#dump file
tb_dump = ["initial begin \n",
           "$dumpfile(\"tb_"+name+".vcd\"); \n",
           "$dumpvars(0,tb_"+name+"); \n",
           "end \n"]

#endmodule
tb_end = ["endmodule \n"]

#locate the design file
tb_loc = ["// Local Variables: \n",
          "// verilog-library-directories:(\"/home/kiran/fpgaProjects/iVerilog/design/"+name+"\") \n",
          "// End:"]

# write all the lines to a single list
tb_content = tb_module + tb_rc + tb_init + tb_clk + tb_dump + tb_end + tb_loc

#write to the file
file.writelines(tb_content)

#close the file
file.close()

#open emacs
try:
    os.system("emacs tb_"+names+".v")
    print("Test-bench successful ;)")
except:
    print("Test-bench failure ;(")
