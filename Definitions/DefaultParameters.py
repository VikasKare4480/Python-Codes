


def demo(a : int, b : int, c : int = 20) -> int:
    print(a)
    print(b)
    print(c)

a = int(input('Enter a : ')) # 10 
b = int(input('Enter b : ')) # 20 
c = int(input('Enter c : ')) # 30

demo(a, b, c) # 10 20 30 
demo(a, b)  # 10 20 20 