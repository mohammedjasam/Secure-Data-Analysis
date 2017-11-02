import math
from functools import reduce

def superMain(SNum, Bits):
    sub1, sub2  = [], []
    preSet = []
    dPreSet = {}
    binRange = []
    bitLen = Bits
    dNumToBin = {}
    dBinToNum = {}
    S, S1, S2, L = [], [], [], []
    string = '{0:0' + str(bitLen) + 'b}' # static BitLength

    # Converts the numeric to binary values!
    for n in SNum:
        bNum = string.format(n)
        S.append(bNum)
        dNumToBin[n] = bNum

    for x in SNum:
        dBinToNum[dNumToBin[x]] = x

    def createPrefix(s, preSet):
        # global dPreSet
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
    def checkLCP(S, pastLCP):
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


        # Replaces the first star with 0 or 1
        LCPrefix = min(countL)[1]
        # print(LCPrefix)

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

    pastS3LCP = []
    def checkS3LCP(S, pastS3LCP):
        LCP = ""
        prefixF = []

        for i in range(len(S)):
            prefixF.append(dPreSet[S[i]])

        LCP = list(reduce(set.intersection, [set(item) for item in prefixF]))

        for x in LCP:
            if x in pastS3LCP:
                LCP.remove(x)

        pastS3LCP += LCP

        c = 0
        countL = []

        for x in LCP:
            countL.append((x.count("*"), x))

        LCPrefix = min(countL)[1]
        print(LCPrefix)
        # Replaces the first star with 0 and 1
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

    def printTheNumbers(mergedL):
        temp1 = mergedL[0]
        temp2 = mergedL[1]
        temp1 = [dBinToNum[x] for x in temp1]
        temp2 = [dBinToNum[x] for x in temp2]

        if len(temp1) >= len(temp2):
            pass
        else:
            temp = temp1[:]
            temp1 = temp2[:]
            temp2 = temp[:]

        # print(temp1, temp2)
        return temp1, temp2

    n = len(S)

    def main(S, pastLCP, pastS3LCP):
        global sub1, sub2
        while (len(S) > math.ceil(n/2)):
            S1, S2 = checkLCP(S, pastLCP)

            if len(S1) >= len(S2):
                L.append(S2)
                S = S1
            else:
                L.append(S1)
                S = S2

        L.append(S)

        mergedL = L[:] ## Has the merged Values of L

        for i in range(0, (len(L)-1)):
            for j in range(i + 1, len(L)):
                if (len(L[i]) + len(L[j])) < math.ceil(n/2):
                    Lij = L[i] + L[j]
                    try:
                        mergedL.remove(L[i])
                        mergedL.remove(L[j])
                        mergedL.append(Lij)
                    except:
                        pass

        if len(mergedL) == 2:
            sub1, sub2 = printTheNumbers(mergedL)
            return sub1, sub2

            # return mergedL
        else:
            # Find S3 via finding the subset who's prefix families share the least number of prefixes!
            pickS3List = []

            for subset in mergedL:
                preFamilies = []
                for x in subset:
                    preFamilies.append(dPreSet[x])
                interSection = list(reduce(set.intersection, [set(item) for item in preFamilies]))
                pickS3List.append((len(interSection), subset))
            S3 = min(pickS3List)[1]
            nS3 = len(S3)
            while (len(mergedL) == 3):
                mergedL.remove(S3)
                print(mergedL)
                # break
                while (len(S3) > math.ceil(nS3/2)):
                    S31, S32 = checkS3LCP(S3, pastS3LCP)
                    print("HI")

                    if len(S31) >= len(S32):
                        L.append(S32)
                        S3 = S31
                    else:
                        L.append(S31)
                        S3 = S32

                ## Assigns bigger list to S1 and vice versa!
                if (len(mergedL[0]) >= len(mergedL[1])):
                    S1 = mergedL[0]
                    S2 = mergedL[1]
                else:
                    S1 = mergedL[1]
                    S2 = mergedL[0]

                ## Assigns smaller list to S31 and vice versa!
                if (len(S31) <= len(S32)):
                    pass
                else:
                    temp = S31[:]
                    S31 = S32[:]
                    S32 = temp[:]

                if (len(S1) + len(S31)) <= math.ceil(n/2):
                    S1 += S31
                    if (len(S2) + len(S32)) <= math.ceil(n/2):
                        S2 += S32
                    else:
                        S3 = S32[:]
                        mergedL.append(S3)
                else:
                    S2 += S31
                    S3 = S32[:]
                    mergedL.append(S3)

            sub1, sub2 = printTheNumbers(mergedL)
            return (sub1, sub2)

    res1, res2 = main(S, pastLCP, pastS3LCP)
    return res1, res2




""" PROGRAM EXECUTION BEGINS """

SNum = [1, 6, 7, 9, 11, 12, 13, 20 , 25, 30]
Bits = 10

# Splits the SNum to two groups based on the algorithm!
res1, res2 = superMain(SNum, Bits)
print(res1, res2)
