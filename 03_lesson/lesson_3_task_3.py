from address_1 import Address
from mailing_1 import Mailing

to_address = Address(f"456022", "Петропавловск",
                     "Пушкина", "25", "15")

from_address = Address(f"424546", "Уфа",
                       f"Гафури", "156", "112" )

mail = Mailing(to_address = to_address,
    from_address = from_address,
    cost = 200,
    track = "TRACK123456789")

print((f"Отправление {mail.track} из {mail.from_address.index},"
       f" {mail.from_address.city}, {mail.from_address.street},"
       f" {mail.from_address.home} - {mail.from_address.flat}"
       f" в {mail.to_address.index}, {mail.to_address.city},"
       f" {mail.to_address.street}, {mail.to_address.home} -"
       f" {mail.to_address.flat}. Стоимость {mail.cost} рублей."))

