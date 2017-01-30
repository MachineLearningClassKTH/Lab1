import monkdata as m
import dtree as d
from  drawtree_qt5 import *




t1 = d.buildTree(m.monk1, m.attributes);
print("\nMONK_1")
print("train: ", d.check(t1, m.monk1))
print("test:  ", d.check(t1, m.monk1test))



t2 = d.buildTree(m.monk2, m.attributes);
print("\nMONK_2")
print("train: ", d.check(t2, m.monk2))
print("test: ", d.check(t2, m.monk2test))



t3 = d.buildTree(m.monk3, m.attributes);

print("\nMONK_3")
print("train: ", d.check(t3, m.monk3))
print("test: ", d.check(t3, m.monk3test))


#drawTree(t1)
drawTree(t2)
#drawTree(t3)
