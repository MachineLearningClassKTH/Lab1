import monkdata as m
import dtree as d
import random
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
