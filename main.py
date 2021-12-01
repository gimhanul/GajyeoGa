import linkedlist

f = linkedlist.boxList()
Anode = linkedlist.node('A')
Bnode = linkedlist.node('B')
Cnode = linkedlist.node('C')
Dnode = linkedlist.node('D')

f.append(Anode)
f.append(Bnode)
f.append(Cnode)
f.insert(Dnode, 1)
f.printAll()