import subprocess
import os
lenOfVector = int(input("Enter the size of the Vectors: "))
lenOfBits = int(input("Enter the number of bits: "))
lenOfBits = lenOfBits + 1

subprocess.call(" python3 MulGen.py " + str(lenOfBits), shell = True)

with open("./Circuits/DotProduct.cir","w") as f:
    for i in range(lenOfVector):
        print(".input a" + str(i)+ " 1 " + str(lenOfBits), file = f)
        print(".input b" + str(i)+ " 2 " + str(lenOfBits), file = f)
    print(".input t 1 " + str(lenOfBits+lenOfBits-1), file = f)
    print(".output DotProduct", file = f)
    s = "DotProduct add "
    for i in range(lenOfVector):
        print(".include<Multiply.cir>.output(Product:prod" + str(i) + ").input(a:a" + str(i) + ",b:b" + str(i) + ")", file = f)

    c = lenOfVector
    for i in range(lenOfVector-1):
        c -= 1
        if (i == 0):
            if (c == 1):
                print("Dot add prod" + str(i) + " prod" + str(i+1), file = f)
            else:
                print("x" + str(i) + " add prod" + str(i) + " prod" + str(i+1), file = f)
        else:
            if (c == 1):
                print("Dot add x" + str(i-1) + " prod" + str(i+1), file = f)
            else:
                print("x" + str(i) + " add x" + str(i-1) + " prod" + str(i+1), file = f)

    print("DotProduct gteu Dot t", file = f)


try:
    os.remove("./Inputs/InputClient.txt")
    os.remove("./Inputs/InputServer.txt")
except:
    pass
subprocess.call(" python3 runhw2.py " + str(lenOfVector), shell = True)
