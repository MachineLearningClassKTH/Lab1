import monkdata as m
import dtree as d
from  drawtree_qt5 import *

#t1 = d.buildTree(m.monk1, m.attributes);
#print("train: ", d.check(t, m.monk1))
#print("test:  ", d.check(t, m.monk1test))
#drawTree(t1)


#t2 = d.buildTree(m.monk2, m.attributes);
#print("train: ", d.check(t2, m.monk2))
#print("test: ", d.check(t2, m.monk2test))
#drawTree(t2)

t3 = d.buildTree(m.monk3, m.attributes);
print("train: ", d.check(t3, m.monk3))
print("test: ", d.check(t3, m.monk3test))
drawTree(t3)
