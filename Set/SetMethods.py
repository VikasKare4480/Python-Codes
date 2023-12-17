

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

# add(object)

set1.add(100)
print('Add', set1)
set1.discard(100)

# copy()


set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

set3 = set1.copy() # set1 is not a nested so follow the deep copy
print('copy', set3)

# deffrence()


set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

difference = set1.difference(set2) # 10 20
print(difference)

# diffence_update()

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print(set1)
print(set2)
set1.difference_update(set2) # set1 becomes the 100 10 20
print("Difference_Update ", set1)

# discard(object)


set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

set1.discard(10)
print('discard(10 ) : {}'.format(set1))

# intersection() -- new set of common objects  


set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

intersectionSet = set1.intersection(set2) 
print('intersectionSet : ', intersectionSet)

# intersection_update() -- chages into same set 

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

set1.intersection_update(set2)
print('intersectionSet : ', set1) 

# isdisjoint() -- bool False if any elements of the A is present in B else returns True

set1 = {10, 20, 30, 40}
set2 = {50}

print('Disjoint : ', set1.isdisjoint(set2)) # True

# isSumset()

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print(set1.issubset(set2)) # True


# issupeset() 

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print(set1.issuperset(set2)) # True

# symmetric_diffence()

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print(set1.symmetric_difference(set2))
set1.symmetric_difference_update(set2)
print(set1)

# union() 

set1 = {10, 20, 30, 40}
set2 = {10, 20, 30, 40}
union = set1.union(set2)
print(union)

# update() adds Set B to Set A

set1 = {10, 20, 30, 40}
set2 = {10, 20, 30, 40}

set1.update(set2)
print(set1)

# pop() removes the top element 

set1 = {10, 20, 30, 40}
print(set1.pop()) # 40 is poped

# clear()

set1 = {10, 20, 30, 40}
set1.clear()
print(set1) # set()




















