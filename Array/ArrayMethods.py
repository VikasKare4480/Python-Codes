
import array as arr



data = arr.array('i', [10,20,30,40])

# properties of array 

# itemsize

print('itemsize' , data.itemsize) # 4 bytes

# typecode

print('typecode ' , data.typecode) # i -- integers


print(data) # array('i',[list of elements])

print(id(data))  # memory of the reffernce data 

# append(object)

data.append(50); # [10, 20, 30, 40, 50]

print(data)

# buffer_info()

print(data.buffer_info()) # memory address of first element with total no of elements

# count(object) couts the no of objects in the array

print('30 : ',data.count(30))

# extend(iterable) -- list || tuple || range 

tuple = (60, 70, 80)

data.extend(tuple)

print(data)

# fromlist() -- appends all list elements to array 

list = [90, 100]

data.fromlist(list)

print(data)

# index(object) -- return index of first occurrence of an object

index = data.index(60)

print('index of  :60 ', index)

# insert(index, object) -- insert a element at the provided position in the array 
#    retunrns None type

insert = data.insert(0, 18)

print(insert) # None

print(data) # [0, other elements in array]

# pop() -- removes last element and returns the poped element
# pop() -- remove and return item (default last)
print('Before pop : ', data)

print('poped : ', data.pop())

print('After pop : ', data)

# remove() -- removes first occurrence of object 

removed = data.remove(90)

print('after remove opration(90) : ', data)

# reverse() -- reverse order of the elements in the array 

data.reverse()

print('after reverse : {}'.format(data))

data.reverse()

# tolist() -- convert array into list

list = data.tolist()

print(list)
print(data)


