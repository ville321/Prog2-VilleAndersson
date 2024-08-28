# for i in range(1000):
#     if i % 7 == 0:
#         print(i)

# text = input("Skriv något: ")
# count = 0

# for char in text:
#     try:
#         number = int(char)
#         count += 1
#     except:
#         pass
# print(count)

number = 2
count = 1
proceed = True

while proceed:
    for i in range(2, number):
        if number % i == 0:
            number += 1
            break
        else:
            count += 1
    if count == 2:
        print(number)
        proceed = False