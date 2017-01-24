import monkdata as m
from dtree import *

# Assignment1 Calculation entropy for each training data sets

print("---Assignment1--- Entropy")
#monk-1
print("monk1: {}".format(entropy(m.monk1)))
#monk-2
print("monk2: {}".format(entropy(m.monk2)))
#monk-3
print("monk3: {}".format(entropy(m.monk3)))

print("\n\n")
#Assignment3
print("--- Assignment3 --- Expected Information gain")
print("Monk1")
print(averageGain(m.monk1, m.attributes[0]))
print(averageGain(m.monk1, m.attributes[1]))
print(averageGain(m.monk1, m.attributes[2]))
print(averageGain(m.monk1, m.attributes[3]))
print(averageGain(m.monk1, m.attributes[4]))
print(averageGain(m.monk1, m.attributes[5]))

print("\n")
print("Monk2")
print(averageGain(m.monk2, m.attributes[0]))
print(averageGain(m.monk2, m.attributes[1]))
print(averageGain(m.monk2, m.attributes[2]))
print(averageGain(m.monk2, m.attributes[3]))
print(averageGain(m.monk2, m.attributes[4]))
print(averageGain(m.monk2, m.attributes[5]))

print("\n")
print("Monk3")
print(averageGain(m.monk3, m.attributes[0]))
print(averageGain(m.monk3, m.attributes[1]))
print(averageGain(m.monk3, m.attributes[2]))
print(averageGain(m.monk3, m.attributes[3]))
print(averageGain(m.monk3, m.attributes[4]))
print(averageGain(m.monk3, m.attributes[5]))
