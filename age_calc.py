user_data = input('Enter your name, lastname, birth year separated by space: ').split(' ')
curr_year = 2021

#age= curr_year - int(birth_year)
#print("Your age is: " + str(age))
#print(f"Your age is {age}")

print(user_data) 
age= curr_year - int(user_data[2])
print("Your age is: " + str(age)