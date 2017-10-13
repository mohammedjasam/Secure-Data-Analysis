import os
import time
import sys



lenOfVector = int(sys.argv[1])
# print("vex are"+ str(sys.argv[1]))
#-------------------------------------------------------------------------------
# Circuit name grabber
try:
    with open("./Circuits/DotProduct.cir","r") as f:
        pass
    cirName = "DotProduct.cir"
except:
    print("\nEnter Circuit name:")
    cirName = input()
#-------------------------------------------------------------------------------
# Inputs into the Client and Server
for i in range(lenOfVector):
    print("\nEnter the value for Client " + str(i))
    with open("./Inputs/InputClient.txt", "a") as text_file:
        a=int(input())
        print("a" + str(i) + " %d" %a, file=text_file)

    print("\nEnter the value for Server "+ str(i))
    with open("./Inputs/InputServer.txt", "a") as text_file:
        b=int(input())
        print("b" + str(i) + " %d" %b, file=text_file)

print("Enter the threshold")
with open("./Inputs/InputClient.txt", "a") as text_file:
    a = int(input())
    print("t " + str(a), file = text_file)

print("\n\n")
#-------------------------------------------------------------------------------
# Command to check the Circuit file
checkCirCMD = "./testfiles ./Circuits/" + cirName
os.system(checkCirCMD)

# Command to run the Circuit File
runCirCMD = "./runtestgcparser ./Circuits/" + cirName +" ./Inputs/InputServer.txt ./Inputs/InputClient.txt"
os.system(runCirCMD)
#-------------------------------------------------------------------------------
# Waits for Client and Server exchange
time.sleep(2)
#-------------------------------------------------------------------------------
# Displays their results
print("\n\n")
print("Client output")
os.system("cat ./results/siclient* | grep Product")
print("\nServer output")
os.system("cat ./results/siserver* | grep Product")
