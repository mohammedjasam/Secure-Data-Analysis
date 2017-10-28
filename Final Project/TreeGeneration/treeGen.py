import math

preSet = []
dPreSet = {}
binRange = []

SNum = [1, 6, 7, 9, 11, 12, 13, 16, 20, 25, 30]
# SNum = [1, 6, 7, 16, 20]
bitLen = 5
S = []
S1, S2, L = [], [], []
string = '{0:0' + str(bitLen) + 'b}' # static BitLength
for n in SNum:
    bNum = string.format(n)
    S.append(bNum)
# print(S)
def createPrefix(s, preSet):
    global dPreSet
    savedS = s
    temp = []  # temp list to generate the Prefix Set of a binary value
    temp.append(s)
    s = list(s)
    for x in range(1, len(s) + 1):
        s[-x] = '*'
        temp.append(''.join(s))
    dPreSet[savedS] = temp
    preSet += temp

def checkMSB(n, b):
    if n[b] == "0":
        return 1
    elif n[b] == "1":
        return 2

SLEN = len(S)
def main():
    global S, S1, S2, L # L

    count = 0
    while (len(S) > math.ceil(SLEN/2)):
        count += 1
        for n in S:
            if checkMSB(n, count) == 1:
                S1.append(n)
            else:
                S2.append(n)
        if len(S1) >= len(S2):
            L.append(S2)
            S = S1
        elif len(S1) <= len(S2):
            L.append(S1)
            S = S2
    L.append(S)
    # print(L)


main()
