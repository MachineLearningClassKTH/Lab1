import monkdata as m
import dtree as d
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from  drawtree_qt5 import *
from treePruner import *

#plot settings
plt.style.use("ggplot")
params = {"legend.fontsize": 6}
plt.rcParams.update(params)

dataset = m.monk1
dataset_test = m.monk1test
mean_times = 100
#fractions = np.linspace(0.3,0.8, 12)
fractions = [0.3,0.4,0.5,0.6,0.7,0.8]

printGraph(fractions, dataset, dataset_test, mean_times)
