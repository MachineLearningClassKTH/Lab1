import monkdata as m
import dtree as d
import random
from  drawtree_qt5 import *

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

monk1train, monk1val = partition(m.monk2, 0.6)


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



print("Validation: ", d.check(current, monk1val))
print("Test: ", d.check(current, m.monk2test))
