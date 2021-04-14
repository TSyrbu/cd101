# lst = [1, -2, 11, 545, 77, 10, 6, -24, 9, 3, 0]
# even = []
# noteven = []
# операторы: <, >, >=, <=, ==, !=, and, or , not

# for val in lst:
#     if val % 2 == 0:
#         even.append(val)
#     else:
#         noteven.append(val)
# print(even)
# print(noteven)

names = []
ages = []
lsts = []
average_age = 0
while True:
    lsts = input("Enter yous name and age: ").split(",")
    names.append(lsts[0])
    ages.append(int(lsts[1]))
    
    status = input("One more? Press Y to continue. Otherwise press N: " )
    if status == "N":
        break

for idx, val in enumerate(names):
    print(f"User {idx}: {val}, {ages[idx]}")
    average_age = (average_age + ages[idx])

print(average_age/len(ages))