import monkdata as m
import dtree as d
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from  drawtree_qt5 import *
from treePruner import *

#plot settings
plt.style.use("ggplot")
font = {"family": "meiryo"}
matplotlib.rc("font", **font)
params = {"legend.fontsize": 6}
plt.rcParams.update(params)

dataset = m.monk1
dataset_test = m.monk1test
mean_times = 20
fractions = [0.3,0.4,0.5,0.6,0.7,0.8]
result = []
for x in fractions:
    error = getMeanError(dataset, dataset_test, x, mean_times);
    result.append(error)
    print("Test for fraction ", x, ": ", error)

plt.plot(fractions, result)
plt.xlabel("fractions")
plt.ylabel("fit(%)")
plt.savefig("../plots/assignment7_monk3.png")
