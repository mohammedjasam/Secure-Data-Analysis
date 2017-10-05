import os
import time
#-------------------------------------------------------------------------------
# Circuit name grabber
try:
    with open("./Circuits/greaterorequal.cir","r") as f:
        pass
    cirName = "greaterorequal.cir"
except:
    print("\nEnter Circuit name:")
    cirName = input()
#-------------------------------------------------------------------------------
# Inputs into the Client and Server
print("\nEnter the value for Client")
with open("./Inputs/InputClient.txt", "w") as text_file:
    a=int(input())
    # print(a.bit_length())
    print("a %d" %a, file=text_file)
# text_file.close()

print("\nEnter the value for Server")
with open("./Inputs/InputServer.txt", "w") as text_file:
    b=int(input())
    # print(b.bit_length())
    print("b %d" %b, file=text_file)
# text_file.close()
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
os.system("cat ./results/siclient* | grep mil")
print("\nServer output")
os.system("cat ./results/siserver* | grep mil")
