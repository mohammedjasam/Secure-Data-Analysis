import sys
import hashlib
# SHA-1 Hash function!
def hashIt(s):
    s = str.encode(s)
    return hashlib.sha1(s).hexdigest()

def searchForME(bloom, vr, trap):
    print("*****************************************************************")
    # print("trap is")
    # print(trap)
    # print("\n")
    # print(bloom)
    # print("\n\n")
    trapCopy = trap[:]
    # print(bloom)
    # print()
    m = len(bloom)
    # print("M is:", str(m))
    total = bloom.count(1)
    counter = 0
    for row in trap:
        for col in row:
            a2 = hashIt(col + str(vr))
            # print("***********************")
            # print(a2)
            # print()
            xa = int(a2, 16)
            # print("M and XA")
            # print(m, xa)
            index = xa % m
            # print("INDEX IS:", str(index))
            if bloom[index-1] == 1:
                print("YAAY")
                print('index is: ' + str(index))
                counter += 1
            elif bloom[index-1] == 0:
                # a=1
                print("LOL its not in range!")
                # return "FAIL"
        # print("=====================> ", str(counter))
    if counter == total:
        print("yaaaaaaa*******************************************************************aaaaaaay")
        # print("result is ")
        # print(trap)
