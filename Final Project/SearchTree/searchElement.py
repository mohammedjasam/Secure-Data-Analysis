import sys
import hashlib
# SHA-1 Hash function!
def hashIt(s):
    s = str.encode(s)
    return hashlib.sha1(s).hexdigest()

def searchForME(bloom, vr, secondhashed, trap):
    # print("*****************************************************************")
    trapCopy = trap[:]
    m = len(bloom)
    traps = []
    for row in trap:
        for col in row:
            a2 = hashIt(col + str(vr))
            # print("Trap is:")
            # print(a2)
            traps.append(a2)
            # xa = int(a2, 16)
            # # print("M and XA")
            # # print(m, xa)
            # index = xa % m
            #
            # print("INDEX IS:", str(index))
            # if bloom[index] == 1:
            #     print("YAAY")
            #     print('index is: ' + str(index))
            #     counter += 1
            #     return "PASS"
            # elif bloom[index] == 0:
            #     return "FAIL"
            #     # a=1
            #     print("LOL its not in range!")
            #     # return "FAIL"
    # print(secondhashed)
    for node in secondhashed:
        for t in traps:
            if t in node:
                # print("YES")
                return "PASS"

                # print("Trap is:")
                # print(a2)
                # print(node)
                # pass
            else:
                # print("BROKE HERE <--------------")
                break
                # break
        # print()
    # print("===============================================================")
