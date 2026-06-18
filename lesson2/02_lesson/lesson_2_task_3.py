a = int(input("Введите число:"))


def square(n):
    area = n ** 2

    if area != int(area):
        return int(area) + 1
    return int(area)


print(square(a))

square(a)
