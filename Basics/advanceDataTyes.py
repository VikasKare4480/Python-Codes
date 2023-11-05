
#List -->> Mutable

'''
    Lists are mutable and stores any type of data
'''

list = [10, 20, 30.00, "Vikas", True]

print(list)
print(type(list))

list[0] = 10.10;
print(list)


#Tuple -->> Immutable

tuple = (10, 20, 30.30, "Viaks", False)
print(type(tuple))

print(tuple)
# tuple[0] = 10.10; #-- >>  Python tuple does not supports the item assignment
print(tuple)

# Range 

x = range(10)
print(type(x))

for i in x:
    print(i, end= " ")

# None -- >> reffernce to nothing

print(None)
print(type(None))

#Set 
''' 
    not contains duplicates values and is a immutable 
    cant get changes once assigned 
    order of insertion is not stored 
    cant remove items
'''

set = {10, 20, 30.30, "Viaks", False}
print(set)
print(type(set))

# set[0] = 10.10 cant supports its assigment
set.add(40) # this is allowed
print(set)

set.remove(20) # this is allowed

print(set)

# Dictionary

'''
    Dictionary is a mutable data structure 
    it stores key-value pair
    key-value pair is a pair of key and value
'''

dict = {
    "name": "Vikas",
    "age": 20,
    "city": "Bangalore"
}

print(dict)

dict["age"] = 30

print(dict)

dict["city"] = "Chennai"

print(dict)

dict.pop("age")

print(dict)

dict.clear()

print(dict)

# Byte

'''
    Byte is a signed 8-bit integer. 
    It is used to represent numbers between -128 and 127.
    It is also used to represent negative numbers.  
    It is also used to represent binary numbers.
    It is also used to represent octal numbers.
    It is also used to represent hexadecimal numbers.
    It is also used to represent floating point numbers.
    It is also used to represent complex numbers.
    It is also used to represent strings.
    Byte is also used to represent unsigned integers.
    It is used to represent numbers between 0 and 255.
    It is also used to represent negative numbers.
    Byte is also used to represent unsigned long integers.
    
'''