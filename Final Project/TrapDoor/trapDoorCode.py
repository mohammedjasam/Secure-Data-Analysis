import sys
import hashlib
sys.path.insert(0, 'C:/Users/Stark/Desktop/Programming/Coursework/Secure-Data-Analysis/Final Project/MinPrefixCode/')
import minPrefixGen as mp # file that generates the minPrefix
# sys.path.insert(0, 'C:/Users/Stark/Desktop/Programming/Coursework/Secure-Data-Analysis/Final Project/BloomFilter/')
# import bloomfilter as bf # file that will generate the bloom filter!

# SHA-1 Hash function!
def hashIt(s):
    s = str.encode(s)
    return hashlib.sha1(s).hexdigest()

# Extract the keys from the treeGen function
randK = tree.getPrivateKeys()

theRange = [1, 8]
minPrefixSet = mp.main(theRange)

trap = []
tempTrap = []
for prefix in minPrefixSet:
    l = []
    ll = []

    for k in randK:
        element = k + prefix
        l.append(hashIt(element))
        ll.append(element)
    trap.append(l) # Contains the hashed values!
    tempTrap.append(ll) # Appends the normal element an primarily used to display

def getTrapDoor():
    return trap


# Prints the hashed values
# for x in trap:
#     print(x)
