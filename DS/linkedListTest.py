import linkedList

f = linkedList.BoxList()
Anode = linkedList.Node('A')
Bnode = linkedList.Node('B')
Cnode = linkedList.Node('C')
Dnode = linkedList.Node('D')

f.append(Anode)
f.append(Bnode)
f.append(Cnode)
f.insert(Dnode, 1)
f.delete(0)
f.printAll()