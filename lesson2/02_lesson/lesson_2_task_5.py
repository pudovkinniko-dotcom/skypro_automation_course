month = int(input("Введите месяц:"))


def month_to_season(m):
    if m in (12, 1, 2):
        return "Зима"
    elif m in (3, 4, 5):
        return "Весна"
    elif m in (6, 7, 8):
        return "Лето"
    elif m in (9, 10, 11):
        return "Осень"
    else:
        return "Неверный номер месяца"


print(month_to_season(month))

month_to_season(month)
