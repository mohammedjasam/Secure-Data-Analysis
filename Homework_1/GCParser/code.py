"""This file will generate the circuit file based on the number of bits specified by the user"""

import os
# Gives execute permissions to the files
os.system("chmod u+x ./testfiles")
os.system("chmod u+x ./runtestgcparser")

# Takes Client and Server inputs
print("Enter the bits in Client")
ClientBit = input()

print("Enter the bits in Server")
ServerBit = input()

# Generates the Circuit file
with open("./Circuits/greaterorequal.cir","w") as f:
    print(".input a 1 " + ClientBit, file = f)
    print(".input b 2 " + ServerBit, file = f)
    print(".output mil", file = f)
    print("mil gteu a b", file = f)

# Calls the runhw1.py file to automate the whole execution process!
import subprocess
subprocess.call(" python3 runhw1.py 1", shell = True)
