import os
import sys


current_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(current_path + "\TreeGeneration")

os.system("python treeGen.py ")
