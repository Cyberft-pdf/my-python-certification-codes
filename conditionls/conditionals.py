x = int(input("What is x?:"))
y= int(input("What is y?:"))


# klasické if, elif, else
if x < y:
    print("x is smaller then y")
elif x > y:
    print("x is bigger then y")
else:
    print("x is equal to y")

#nebo použít "or"    
if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")    

#také můžeme použít "and"    
score = int(input("Score: "))


if score >= 90 and score <= 100:
    print("Grade: A")
if score >= 80 and score < 90:
    print("Grade: B")
if score >= 70 and score < 80:
    print("Grade: C")
if score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")


#modulo
    
x = int(input("what is x?:"))

def main():
    x = int(input("what is x?:"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    """
    if x % 2 == 0:
        return True
    else:
        return False
    """
    """
    return True if n % 2 == 0 else False
    """
    return n % 2 == 0 

#match = podobné switch jako v Cx

name = input("Whats your name?: ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")