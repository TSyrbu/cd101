f_name = [] #'Ludwig v.', 'Johann', 'Wilfgang', 'Richarg', 'Pyotor','Giuseppe','Igor', 'Johann', 'Sergei', 'Franz'
l_name = [] #'Beethoven','Bach','Mozart','Wagner','Tchaikovsky','Verdi','Stravinsky','Strauss','Rachmaninoff','Shubert'
b_year = [] #1770, 1685, 1756, 1813, 1840, 1813, 1882, 1825, 1873, 1797
d_year = [] #1827, 1750, 1791, 1883, 1893, 1901, 1971, 1899, 1943, 1828
age = []
average_age = 0
flbd = []

def composers(z):
    print(f"№{z}")
    flbd = input("Enter composer first neme, last name, year of birth and death: ").split(" ")
    return(flbd)
def composers_age(b,d):
    for n in range(len(b)):
        age.append(d[n]-b[n])
    return(age)
def age_average(a):
    summ = 0 
    for m in range(len(a)):
        summ= summ+a[m]
        average_age=summ/len(a)
    return(average_age)


i=1   
q1=input("Hello User! Would you like to add composers? If yes press 1: ")
if q1 == "1":
    while True:
        flbd=composers(i)
        f_name.append(flbd[0])
        l_name.append(flbd[1])
        b_year.append(int(flbd[2]))
        d_year.append(int(flbd[3]))
        status = input("One more? Press any key to continue. Otherwise press 0: " )
        if status == "0":
            break
        else:
            i+=1
            continue
q2=input("Would you like to calculate age? If yes press 1:")
if q2 == "1":
    age = composers_age(b_year,d_year)
    average_age = age_average(age)
    data = {"first":f_name, "last":l_name, "ages":age, "average":average_age}
    print("First name: ", data["first"])
    print("Last name: ", data["last"])
    print("Age: ", data["ages"])
    print("Average: ",data["average"])
    print("Thank you for useing! Have a nice day")
else:
    for d in range(i):
        print("First name: ", f_name[d])
        print("Last name: ", l_name[d])
    print("Thank you for useing! Have a nice day")




