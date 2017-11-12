import sys
sys.path.insert(0, 'C:/Users/Stark/Desktop/Programming/Coursework/Secure-Data-Analysis/Final Project/TreeGeneration/')
import treeGen as tree
import random
import hashlib

SNum = [6, 7]
unionSet = []
S = []
bitLen = 4
preset = []
appendFirst = []
hashedAppendFirst = []
randK = []


# SHA-1 Hash function!
def hashIt(s):
    s = str.encode(s)
    return hashlib.sha1(s).hexdigest()

# generate random values!
for i in range(7):
    randK.append(str(random.randint(1, 1000)))

# Convert to fixed length binary!
string = '{0:0' + str(bitLen) + 'b}' # static BitLength

for n in SNum:
    bNum = string.format(n)
    S.append(bNum)

# Creating the prefix set!
for element in S:
    tree.genPrefix(element, preset)

# Taking union of prefix set!
unionSet = list(set(preset))

# Each node has a random value
vr = random.randint(1, 1000)

# print(unionSet)
print()

# For every element in unionSet create the hashed values of the elements for some N iterations!
for prefix in unionSet:
    l = []
    hl = []
    for index, num in enumerate(randK):
        K = randK[index] + prefix
        l.append(K)
        hk = hashIt(K)
        # hK = hashIt(K) + str(vr)
        # hhKvr = hashIt(hk)
        hl.append(hk)
    appendFirst.append(l)
    hashedAppendFirst.append(hl)

print("The random K are:")
print(randK)
print()


# for x in range(len(unionSet)):
#     print(unionSet[x], appendFirst[x], hashedAppendFirst[x])
# for x in appendFirst:
#     print(x)
#
for x in hashedAppendFirst:
    print(x)

# tree.getTree()
