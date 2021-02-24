F_name = [] #'Ludwig v.', 'Johann', 'Wilfgang', 'Richarg', 'Pyotor','Giuseppe','Igor', 'Johann', 'Sergei', 'Franz'
L_name = [] #'Beethoven','Bach','Mozart','Wagner','Tchaikovsky','Verdi','Stravinsky','Strauss','Rachmaninoff','Shubert'
B_year = [] #1770, 1685, 1756, 1813, 1840, 1813, 1882, 1825, 1873, 1797
D_year = [] #1827, 1750, 1791, 1883, 1893, 1901, 1971, 1899, 1943, 1828
age = []
average_age = 0
n = int(input("Enter the number of composers: "))

for x in range(n):
    F_name.append(input("Enter composer first name: "))
    L_name.append(input("Enter composer last name: "))
    B_year.append(input("Enter the year of birth: "))
    D_year.append(input("Enter the year of death: "))
    age.append(int(D_year[x])-int(B_year[x]))
    average_age = (average_age + age[x])
for z in range(n):
    print(f"First name: {F_name[z]} Last name: {L_name[z]} Age: {age[z]}")

print(average_age//n)
