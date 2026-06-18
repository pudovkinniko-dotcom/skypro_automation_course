from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "+79111234567"),
    Smartphone("Samsung", "Galaxy S24", "+79221234567"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79331234567"),
    Smartphone("Google", "Pixel 8", "+79441234567"),
    Smartphone("Asus", "Zenfone 10", "+79551234567")
]


for smartphone in catalog:
    print(f"{smartphone.brand} {smartphone.model} - {smartphone.phone_number}")
