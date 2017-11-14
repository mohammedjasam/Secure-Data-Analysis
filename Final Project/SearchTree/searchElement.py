import sys
import hashlib
# SHA-1 Hash function!
def hashIt(s):
    s = str.encode(s)
    return hashlib.sha1(s).hexdigest()

def searchForME(bloom, vr, trap):
    print("trap is")
    print(trap)
    trapCopy = trap[:]
    # print(bloom)
    print()
    m = len(trap)
    total = bloom.count(1)
    counter = 0
    for row in trap:
        for col in row:
            index = hashIt(col + str(vr))
            index = int(index, 16) % m
            if bloom[index] == 1:
                # print('index is' + str(index))
                counter += 1
                pass
            elif bloom[index] == 0:
                a=1
                # print("LOL its not in range!")
                # return "FAIL"
        # print("=====================> ", str(counter))
    if counter == total:
        print("yaaaaaaa*******************************************************************aaaaaaay")
        print("result is ")
        print(trap)
