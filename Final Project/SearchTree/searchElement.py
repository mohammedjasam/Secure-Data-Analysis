import sys
import hashlib

# SHA-1 Hash function!
def hashIt(s):
    s = str.encode(s)
    return hashlib.sha1(s).hexdigest()

def searchForME(bloom, vr, secondhashed, trap, SNUM):
    trapCopy = trap[:]
    m = len(bloom)
    total = bloom.count(1)
    counter = 0

    for row in trap:
        for col in row:
            twoTimeHash = hashIt(col + str(vr))
            # print(twoTimeHash) # Prints the hash with vr
            xa = int(twoTimeHash, 16)
            index = xa % m
            # print(trap)
            if bloom[index] == 1:
                return "PASS"
            else:
                break
