class Address:

    def __init__(self, index, city, street, home, flat):
        self.index = index
        self.city = city
        self.street = street
        self.home = home
        self.flat = flat

    def __str__(self):
        return (f"{self.index} город: {self.city},"
                f" улица: {self.street}  номер дома: {self.home},"
                f" квартира: {self.flat}")
