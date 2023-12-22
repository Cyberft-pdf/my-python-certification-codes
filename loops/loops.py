#while

i = 0

while i < 3:
    print("Mew")
    i += 1


#for 

for i in range(8):
    print("meow")


# "_" mi značí že tu proměnou nepotřebuji k ničemu jinému než aby to fungovalo (nikde jinde ji nepoužívám/nepracuji)
for _ in range(8):
    print("meow")


print("meow\n" * 3 , end="")

#validation input (continue, break)
while True:
    n = int(input("What is n ?:"))
    if n > 0:
        break

for _ in range(n):
    print("meow")   
