#funkci dělám proto abych nemusela něco psát několikrát, takhle to jenom zavolám 

"""
def hello(to = "world"):
    print("hello word", to)

hello()

name = input("Whats your name? ")

hello(name)
"""


#scope
"""
def main():
    name = input("What is your name?")
    hello()


#u funkcí nemůžu použít proměnou kterou si stanovím v jiné funkci bez použití return
def hello():
    print("Hello", name)
"""

def main():
    x = int(input("What is x?: "))
    print("x squared is", square(x))

def square(n):
    return n *n 

main()