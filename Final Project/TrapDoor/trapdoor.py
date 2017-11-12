import sys
sys.path.insert(0, 'C:/Users/Stark/Desktop/Programming/Coursework/Secure-Data-Analysis/Final Project/MinPrefixCode/')
import minPrefixGen as mp # file that will generate the bloom filter!


minPrefixSet = mp.getMinPrefixSet([1, 8])
print(minPrefixSet)
