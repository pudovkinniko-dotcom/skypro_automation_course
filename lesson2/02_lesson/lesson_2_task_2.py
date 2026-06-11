def is_year_leap(year):
    return year % 4 == 0


current_year = 2028
is_leap = is_year_leap(current_year)

print(f"год {current_year}: {is_leap}")
