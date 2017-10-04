print("Enter the bits in Client")
ClientBit = input()

print("Enter the bits in Server")
ServerBit = input()

with open("./Circuits/Gen.cir","w") as f:
    print(".input a 1 " + ClientBit, file = f)
    print(".input b 2 " + ServerBit, file = f)
    print(".output Gen", file = f)

    for i in range(int(ClientBit)):
        print("a"+str(i)+" select a "+str(i)+" "+str(i+1), file =f)

    for i in range(int(ServerBit)):
        print("b"+str(i)+" select b "+str(i)+" "+str(i+1), file =f)

    for j in range(int(ServerBit)):
        st = "aandbs" + str(j) + " concat "
        for i in range(int(ClientBit)):
            print("aandb" + str(j) +"c"+ str(i) + " and a" + str(i) + " b" + str(j), file = f)
        s="aandb" + str(j) + "temp" + " concat "
        for k in range(int(ClientBit)-1,-1,-1):
            s += "aandb" + str(j) + "c" + str(k) + " "
            l = ""
            r = ""
            for a in range(int(ClientBit)-j-1,0,-1):
                l += "0 "
            for b in range(int(ClientBit)-int(len(l)/2)):
                if not(b == 0):
                    r += "0 "
            fin = st + l + "aandb" + str(j) + "temp " + r

        print(s, file = f)
        print(fin, file = f)


    for adding in range(int(ClientBit)-1):
        if (adding == int(ClientBit) - 2):
            if adding == 0:
                print("Gen" + " add " + "aandbs" + str(adding) + " aandbs" + str(adding+1), file = f)
            else:
                print("Gen" + " add " + "sum" + str(adding-1) + " aandbs" + str(adding+1), file = f)
        elif adding == 0:
            print("sum"+str(adding) + " add " + "aandbs" + str(adding) + " aandbs" + str(adding+1), file = f)
        else:

            print("sum"+str(adding) + " add " + "sum" + str(adding-1) + " aandbs" + str(adding+1), file = f)
import subprocess
subprocess.call(" python3 code.py 1", shell = True)
# import os
# os.system("python3 code.py 1", shell = True)
