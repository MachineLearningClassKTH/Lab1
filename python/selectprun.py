import monkdata as m
import dtree as d
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from  drawtree_qt5 import *
from treePruner import *


#dataset = m.monk1
#dataset_test = m.monk1test
iteration = 100
#fractions = np.linspace(0.3,0.8, 12)
fractions = [0.3,0.4,0.5,0.6,0.7,0.8]

meanMonk1, varMonk1 = calculateFitness(fractions, m.monk1, m.monk1test, iteration, 1)
meanMonk2, varMonk2 = calculateFitness(fractions, m.monk2, m.monk2test, iteration, 2)

#plotData
results = np.array([meanMonk1, meanMonk2])
plotData(results, fractions)


