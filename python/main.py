import monkdata as m
from dtree import *

# Assignment1 Calculation entropy for each training data sets

#monk-1
entropyMonk1 = entropy(m.monk1)
#monk-2
entropyMonk2 = entropy(m.monk2)
#monk-3
entropyMonk3 = entropy(m.monk3)

print(entropyMonk1)
print(entropyMonk2)
print(entropyMonk3)



#Assignment3
averageGain()

