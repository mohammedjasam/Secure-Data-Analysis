import sys
import hashlib
# SHA-1 Hash function!
def hashIt(s):
    s = str.encode(s)
    return hashlib.sha1(s).hexdigest()

def searchForME(bloom, vr, secondhashed, trap):
    print("*****************************************************************")

    trapCopy = trap[:]
    print(bloom)
    # print(trap)
    m = len(bloom)
    # print("M is:", str(m))
    total = bloom.count(1)
    counter = 0
    for row in trap:
        for col in row:
            a2 = hashIt(col + str(vr))
            # print("***********************")
            print(a2)
            # print()
            xa = int(a2, 16)
            # print("M and XA")
            # print(m, xa)
            index = xa % m

            print("INDEX IS:", str(index))
            if bloom[index] == 1:
                print("YAAY")
                print('index is: ' + str(index))
                counter += 1
                return "PASS"
            elif bloom[index] == 0:
                return "FAIL"
                # a=1
                print("LOL its not in range!")
                # return "FAIL"
        # print("=====================> ", str(counter))
    if counter == total:
        print("yaaaaaaa*******************************************************************aaaaaaay")
        # print("result is ")
        # print(trap)
