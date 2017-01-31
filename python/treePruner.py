import monkdata as m
import dtree as d
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from  drawtree_qt5 import *

#plot settings
plt.style.use("ggplot")
params = {"legend.fontsize": 6}
plt.rcParams.update(params)

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

def getMeasure(data,datatest, fraction, times):
    errorList = []
    for i in range(0, times-1):
        prunedTree = prune(data,fraction);
        errorList.append(d.check(prunedTree,datatest))
    return np.mean(errorList), np.var(errorList)

def calculateFitness(fractions, dataset, dataset_test, iteration, dataFlag):
    resultMean = []
    resultVar = []
    for x in fractions:
        mean, var = getMeasure(dataset, dataset_test, x, iteration);
        resultMean.append(mean)
        resultVar.append(var)
        print("Test for fraction ", x, ": ", mean)
        print("variance", var)

    #save data
    print('Saved to ../data/monk{}_mean.txt'.format(dataFlag));
    np.savetxt('../data/monk{}_mean.txt'.format(dataFlag), resultMean)
    print('Saved to ../data/monk{}_var.txt\n'.format(dataFlag));
    np.savetxt('../data/monk{}_var.txt'.format(dataFlag), resultVar)
    return resultMean, resultVar

def plotData(results, fractions):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(0, len(results)):
        plt.plot(fractions, results[i], label="monk{}".format(i+1))
        roundedResult = ['%.2f' % ele for ele in results[i]]
        for xy in zip(fractions, roundedResult):
            ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
    plt.xlabel("fractions")
    plt.ylabel("fit(%)")
    plt.ylim((0.4, 1.0))
    plt.legend(fontsize=12)
    plt.savefig("../plots/assignment7.png")
    print("Saved to ../plots/assignment7.png")

