from address import Address
from mailing import Mailing

# Создаем адреса отправления и получения
address_from = Address("101000", "Москва", "ул. Мясницкая", "1", "15")
address_to = Address("443000", "Самара", "ул. Ленинская", "120", "4")

# Создаем экземпляр почтового отправления
mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=350.50,
    track="RU123456789"
)

# Выводим информацию в консоль
print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city},"
      f"{mailing.from_address.street}, {mailing.from_address.house} - "
      f"{mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
