from smartphone import Smartphone

smartphone_1 = Smartphone("Samsung", "A - 52", "+79876543211")

smartphone_2 = Smartphone("Apple", "iphone - 13", "+79781234561" )

smartphone_3 = Smartphone("Lenovo", "P-65", "+79998765432")

smartphone_4 = Smartphone( "{Xiaomi", "Poco C-65", "+79887654321" )

smartphone_5 = Smartphone( "Honor", "Magic 7 pro", "+79871112223")

catalog = [smartphone_1, smartphone_2, smartphone_3, smartphone_4, smartphone_5]

for smartphone in catalog:

    print(f"{smartphone.brand}, {smartphone.model}, {smartphone.number}")