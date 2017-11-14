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
    # print(randK)

    # Each node has a random value
    vr = random.randint(1, 1000)
    # print(vr)
    def getVR():
        return vr
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
        # print('preset is')
        # print(preSet)
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
    lol = []
    mainLol = []
    print(len(unionSet))
    print(unionSet)
    # For every element in unionSet create the hashed values of the elements for some N iterations!
    for prefix in unionSet:
        l = []
        hl = []
        lol = []
        for index, num in enumerate(randK):
            K = randK[index] + prefix
            l.append(K)
            # hal = hashIt(K)
            # hl.append(hk)
            hK = hashIt(K)
            lol.append(hK)
            hK += str(vr)
            hhKvr = hashIt(hK)
            hl.append(hhKvr)
        appendFirst.append(l)
        mainLol.append(lol)
        hashedAppendFirst.append(hl)

    # m value to create the bloomfilter
    m = 10 * len(unionSet)

    bloomFilter = []
    # Creating an array with default value as 0
    for i in range(m):
        bloomFilter.append(0)
    # print(bloomFilter)
    print("initial is")

    print(mainLol)
    # Setting 1 to every index pointed by the mod operation!
    for sett in hashedAppendFirst:
        for x in sett:
            a = int(x, 16)
            i = a % m
            # print(i)
            bloomFilter[i - 1] = 1
    # print("Bloom and VR in bf file")
    # print(bloomFilter, vr)
    return bloomFilter, vr
