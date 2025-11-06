class User:

    def __init__(self, first_name, last_name):
        self.first_Name = first_name
        self.last_Name = last_name

    def name(self):
        print(self.first_Name)

    def last_name(self):
        print(self.last_Name)

    def user_name(self):
        print(f"Имя: {self.first_Name}, фамилия: {self.last_Name}")

