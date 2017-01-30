import monkdata as m
import dtree as d
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from  drawtree_qt5 import *

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

def prune(data, fraction):

    monk1train, monk1val = partition(data, fraction)
    t1 = d.buildTree(monk1train, m.attributes);
    current = t1;
    errorVal = 0;
    while (True):
        old = current;
        listOfSubs = d.allPruned(current);
        for x in listOfSubs:
            if errorVal <= d.check(x, monk1val):
                errorVal = d.check(x, monk1val);
                current = x
        if (old == current):
            break;
    return current

def getMeanError(data,datatest, fraction, times):
    errorList = []
    for i in range(0, times-1):
        prunedTree = prune(data,fraction);
        errorList.append(d.check(prunedTree,datatest))
    return np.mean(errorList)

def printGraph(fractions, dataset, dataset_test, mean_times):
    result = []
    for x in fractions:
        error = getMeanError(dataset, dataset_test, x, mean_times);
        result.append(error)
        print("Test for fraction ", x, ": ", error)

    plt.plot(fractions, result)
    plt.xlabel("fractions")
    plt.ylabel("fit(%)")
    plt.savefig("../plots/assignment7_monk3.png")
    print("Saved to ../plots/assignment7_monk3.png")
