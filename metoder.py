# def summa(*tal):
#     summa = 0
#     for i in range(len(tal)):
#         summa += tal[i]
#     return summa

# print(summa(1, 2, 3,))

def food(s, vegan=False):
    if vegan:
        print("soja" + s)
    else:
        print(s)

food("mjölk")