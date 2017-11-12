import random
import hashlib

SNum = [6, 7]

def getBloomFilter(SNum, Bits, randK):
    unionSet = []
    S = []
    bitLen = Bits
    preset = []
    appendFirst = []
    hashedAppendFirst = []
    print(randK)
    # Each node has a random value
    vr = random.randint(1, 1000)
    print(vr)

    # SHA-1 Hash function!
    def hashIt(s):
        s = str.encode(s)
        return hashlib.sha1(s).hexdigest()

    # Creates the prefixes
    def genPrefix(s, preSet):
        savedS = s # Copy of the S
        temp = []  # temp list to generate the Prefix Set of a binary value

        temp.append(s)

        s = list(s)
        for x in range(1, len(s) + 1):
            s[-x] = '*'
            temp.append(''.join(s))
        preSet += temp

        return preSet

    # Convert to fixed length binary!
    string = '{0:0' + str(bitLen) + 'b}' # static BitLength

    for n in SNum:
        bNum = string.format(n)
        S.append(bNum)

    # Creating the prefix set!
    for element in S:
        genPrefix(element, preset)

    # Taking union of prefix set!
    unionSet = list(set(preset))


    # print()
    # print("UnionSet is: ")
    # print(unionSet)
    # print()
    # print("VR is:")
    # print(vr)
    # print()

    # For every element in unionSet create the hashed values of the elements for some N iterations!
    for prefix in unionSet:
        l = []
        hl = []
        for index, num in enumerate(randK):
            K = randK[index] + prefix
            l.append(K)
            # hk = hashIt(K)
            # hl.append(hk)
            hK = hashIt(K) + str(vr)
            hhKvr = hashIt(hK)
            hl.append(hhKvr)
        appendFirst.append(l)
        hashedAppendFirst.append(hl)

    # print("The random K are:")
    # print(randK)
    # print()

    # m value to create the bloomfilter
    m = 10 * len(unionSet)

    bloomFilter = []
    for i in range(m):
        bloomFilter.append(0)
    # print(bloomFilter)

    for sett in hashedAppendFirst:
        for x in sett:
            a = int(x, 16)
            i = a % m
            # print(i)
            bloomFilter[i - 1] = 1

    return bloomFilter
