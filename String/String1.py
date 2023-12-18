
name = input('Enter Your Name : ')

# String methods

# capitalise(obj) -> str

print(name.capitalize())

# casefold() -- toLowerCase() -> str all chracters to lower case 

print(name.casefold()) 

# center() -- ( 5spaces  name  5 spaces )

print(name.center(10))

# count(obj) -> int

print(name.count('V'))

# encoding() -- on hold by sir

# name.encode('encode')

print(name)

# endswith(str)  -> bool
print('endswith() : ')
print(name.endswith('as')) # True
print(name.endswith('py')) # False

# expadtabs() -> str

print('Expandtabs() : ')
tabsString = 'Vikas\tLaxman\tKare\nSr. Software Developer at Google'
print(tabsString.expandtabs())

# find() -> index
print('find() : ')
print(name.find('k'))

# rfind(str)

print(name.rfind('kare'))

# index(obj)

print(name.index('a'))

# isascii() 

print(name.isascii())

# isdecimal() 

num = "110"
print('isdecimal() : ')
print(name.isdecimal())
print(num.isdecimal())

# isdigit() 

print('isdigit() : ')
print(num.isdigit())

# join('#', str)

print('Join() : ')
print(' '.join(name))

# ljust() 

city = 'Pune' # Pune******

print(city.ljust(10, '*'))
print(city.rjust(10, '*'))

# strip() -> str ->> is like a trim() method in JS

c2w = '   Core2Web  '
print(c2w.strip()) # space of both the sides 
print(c2w.rstrip()) # space of right side get removed 
print(c2w.lstrip()) # space of left side get removed 

# partition(str)

institute = 'Core2Web'
print('Partition() : ')
print(institute.partition('2')) # ('Core', '2', 'Web')

print('rpartition() : ')
print(institute.rpartition(' '))

# split(str)

split = 'String.To.Split'

print(split.split('.'))

# split the input values by the split(str) method

x, y, z = [int(num) for num in input('Enter the 3 int values with space as a  : ').split(' ')]

print(x, y, z)
print(x+y+z)



























