print("Enter the bits in Client")
ClientBit = input()

print("Enter the bits in Server")
ServerBit = input()

with open("./Circuits/greaterorequal.cir","w") as f:
    print(".input a 1 " + ClientBit, file = f)
    print(".input b 2 " + ServerBit, file = f)
    print(".output gteq", file = f)
    print("gteq gteu a b", file = f)
