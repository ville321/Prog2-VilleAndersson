numbers = input("Skriv två siffror: ")
a, b = numbers.split()
a = int(a)
b = int(b)
if(a < b):
    print(a, b)
else:
    print(b, a)