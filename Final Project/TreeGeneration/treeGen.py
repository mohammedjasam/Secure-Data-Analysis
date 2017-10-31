import math
from functools import reduce
preSet = []
dPreSet = {}
binRange = []
bitLen = 5
# dictPrefix = {}

SNum = [1, 6, 7, 9, 11, 12, 13, 16, 20, 25]
# SNum = [1, 6, 7, 16, 20]

S, S1, S2, L = [], [], [], []
string = '{0:0' + str(bitLen) + 'b}' # static BitLength

# Converts the numeric to binary values!
for n in SNum:
    bNum = string.format(n)
    S.append(bNum)


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
    return preSet

for element in S:
    createPrefix(element, preSet)

# for k, v in dPreSet.items():
#     print(k, v)




pastLCP = []
def checkLCP(S):
    global pastLCP

    LCP = ""
    prefixF = []
    for i in range(len(S)):
        prefixF.append(dPreSet[S[i]])

    LCP = list(reduce(set.intersection, [set(item) for item in prefixF]))

    for x in LCP:
        if x in pastLCP:
            LCP.remove(x)

    pastLCP += LCP

    c = 0
    countL = []
    for x in LCP:
        countL.append((x.count("*"), x))

    LCPrefix = min(countL)[1]
    print(LCPrefix)

    LCP0 = list(LCPrefix)
    LCP1 = list(LCPrefix)

    for x in range(len(LCP0)):
        if LCP0[x] == "*":
            LCP0[x] = "0"
            break
    for x in range(len(LCP1)):
        if LCP1[x] == "*":
            LCP1[x] = "1"
            break

    LCP0 = "".join(LCP0)
    LCP1 = "".join(LCP1)

    L0 = []
    L1 = []
    for i in range(len(S)):
        prefixFamily = dPreSet[S[i]]
        if LCP0 in prefixFamily:
            L0.append(S[i])
        else:
            L1.append(S[i])
    return L0, L1

n = len(S)

def main():

    global S, S1, S2, L

    while (len(S) > math.ceil(n/2)):
        S1, S2 = checkLCP(S)

        if len(S1) >= len(S2):
            L.append(S2)
            S = S1
        else:
            L.append(S1)
            S = S2

    L.append(S)
    print(L)

main()
