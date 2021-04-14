import math 
def avg_age(ages):
    return sum(ages) / len(ages)

def distance(a,b):
    return math.sqrt(math.pow(b[0]-a[0],2)+
                     math.pow(b[1]-a[1],2)+
                     math.pow(b[2]-a[2],2))

if __name__=="__main__":
    print(avg_age([12 ,24, 18, 36]))


