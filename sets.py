simple=set()
print(simple,type(simple))

simple={'a','b','d','c','s','a'}

print(simple)
simple.add(3)#mutabul object
print(simple)

set1={'a','b','c','z'}
set2={'1','a','b','c'}
print(set1.intersection(set2))
print(set1.difference(set2))
set1.difference_update(set2)
print(set1)
all_elements=set1.union(set2)

print(set1,set2,all_elements)
