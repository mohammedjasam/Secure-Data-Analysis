import os
import time
#-------------------------------------------------------------------------------
# Circuit name grabber
print("\nEnter Circuit name:")
cirName = input()
#-------------------------------------------------------------------------------
# Inputs into the Client and Server
print("\nEnter the value for Client")
with open("./Inputs/InputClient.txt", "w") as text_file:
    b=int(input())
    print("a %d" %b, file=text_file)
text_file.close()

print("\nEnter the value for Server")
with open("./Inputs/InputServer.txt", "w") as text_file:
    a=int(input())
    print("b %d" %a, file=text_file)
text_file.close()
#-------------------------------------------------------------------------------
# Command to check the Circuit file
checkCirCMD = "./testfiles ./Circuits/" + cirName
os.system(checkCirCMD)

# os.system("../")
# os.system("ls")
# Command to run the Circuit File
runCirCMD = "./runtestgcparser ./Circuits/" + cirName +" ./Inputs/InputServer.txt ./Inputs/InputClient.txt"
os.system(runCirCMD)
#-------------------------------------------------------------------------------
# Waits for Client and Server exchange
time.sleep(2)

# Displays their results
os.system("cat ./results/si*")
