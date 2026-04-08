# Break
# numbers = list(range(0,100))
# for number in numbers:
#     if number > 20:
#         break
#     print(number)
# while True:
#     num =input("Enter The Number (q For Quite) :")
#     # if we enter q it will quite loop
#     if num =='q' :
#         break
#     print(num)

# continue
for i in range(5):
    if i == 2 or i == 4:
        continue
    print(i)