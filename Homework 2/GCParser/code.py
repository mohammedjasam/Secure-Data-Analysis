import os
import time
#-------------------------------------------------------------------------------
# Circuit name grabber
print("\nEnter Circuit name:")
cirName = input()
#-------------------------------------------------------------------------------
# Inputs into the Client and Server
print("\nEnter the value for Client")
with open("Client.txt", "w") as text_file:
    b=int(input())
    print("a %d" %b, file=text_file)

print("\nEnter the value for Server")
with open("Server.txt", "w") as text_file:
    a=int(input())
    print("b %d" %a, file=text_file)
#-------------------------------------------------------------------------------
# Command to check the Circuit file
checkCirCMD = "./testfiles " + cirName
os.system(checkCirCMD)

# Command to run the Circuit File
runCirCMD = "./runtestgcparser " + cirName +" Server.txt Client.txt"
os.system(runCirCMD)
#-------------------------------------------------------------------------------
# Waits for Client and Server exchange
time.sleep(2)

# Displays their results
os.system("cat ./results/si*")
