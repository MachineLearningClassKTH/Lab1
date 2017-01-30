import monkdata as m
import dtree as d
import random
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

fractions = [0.3,0.4,0.5,0.6,0.7,0.8]
for x in fractions:
    prunedTree = prune(m.monk3,x);
    print("Test for fraction ", x, ": ", d.check(prunedTree, m.monk3test))
