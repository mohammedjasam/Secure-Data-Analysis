import os
import time
import sys

#-------------------------------------------------------------------------------
def givePermissions():
    testFile = "chmod u+x testfiles"
    runTestGCParser = "chmod u+x runtestgcparser"
    os.system(testFile)
    os.system(runTestGCParser)

lenOfVector = int(sys.argv[1])
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
print("\nEnter elements separated by commas")
s1 = input("Vector 1: ").split(",")
s2 = input("Vector 2: ").split(",")
s1 = [int(x) for x in s1[:lenOfVector]]
s2 = [int(x) for x in s2[:lenOfVector]]

for i in range(len(s1)):
    with open("./Inputs/InputClient.txt", "a") as text_file:
        print("a" + str(i) + " %d" %s1[i], file=text_file)

    with open("./Inputs/InputServer.txt", "a") as text_file:
        print("b" + str(i) + " %d" %s2[i], file=text_file)

with open("./Inputs/InputClient.txt", "a") as text_file:
    a = int(input("\nEnter the threshold: "))
    print("t " + str(a), file = text_file)

print("\n")
#-------------------------------------------------------------------------------

# givePermissions()

# Command to check the Circuit file
checkCirCMD = "./testfiles ./Circuits/" + cirName
os.system(checkCirCMD)

# Command to run the Circuit File
runCirCMD = "./runtestgcparser ./Circuits/" + cirName +" ./Inputs/InputServer.txt ./Inputs/InputClient.txt"
os.system(runCirCMD)
#-------------------------------------------------------------------------------
# Waits for Client and Server exchange
print("Sleeping for 5 seconds to complete execution")
time.sleep(5)
#-------------------------------------------------------------------------------
# Displays their results
print("\n")
print("Client output")
os.system("cat ./results/siclient* | grep Product")
print("\nServer output")
os.system("cat ./results/siserver* | grep Product")
