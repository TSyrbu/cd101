class User:
    def __init__(self, first_name, last_name,birth,sex):
        self.first_name= first_name
        self.last_name = last_name
        self.birth = birth
        self.sex = sex

    def grit(self):
        print(f"name: {self.first_name}, {self.last_name}, year: {self.birth}")
    
    def calc_age(self,curr_year):
        return curr_year - self.birth
    
    @staticmethod
    def calc_avg(self, other):
        z = self.calc_age(2021)+other.calc_age(2021) / 2
        return z


user1 = User("a", "b", 1980, "male")
user2 = User("c", "d", 1990, "female")

User.calc_avg(user1,user2)