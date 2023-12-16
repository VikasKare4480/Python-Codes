
playersInfo = dict({45: 'Rohit', 77: 'Shubman', 18: 'Virat', 7: 'MSDhoni'})
print(playersInfo)

# get(key)

print(playersInfo.get(77)) # if not found then returns the None

# items() -- key value players 

for key, value in playersInfo.items():
    print(key, " : ", value)

print(playersInfo.items())

# keys() -->> returns the set of the key 

print(type(playersInfo.keys())) # <class 'dict_keys'>

# values() -->> set of values 

print(type(playersInfo.values()))  # <class 'dict_values'>

# popitem() -- >> removes the last key-value pair

playersInfo.popitem()

print(playersInfo)

# pop(key) --> removes key value of provided k-v pair

playersInfo.pop(45) 

print(playersInfo)

# update(ietrable / dict)

dict = {45 : "Rohit", 10 : "Sachin Tendulkar"}
playersInfo.update(dict)
print(playersInfo)


# copy() 

playersInfoCopy = playersInfo.copy()
print(playersInfoCopy)

# clear() 

playersInfoCopy.clear()
print(playersInfoCopy)

# setdefault()

print(playersInfo.setdefault(45))
print(playersInfo)

# fromkeys()

lang = ["Java", "Cpp", "Python", "Flutter"]
teacher = "Shashi";

print(playersInfo.fromkeys(lang, teacher))



























