for x in range(1, 31):
    print("x = ", x, " x² = ", x*x)

students = ["Александр", "Михаил", "Мария", "Ольга", "Кирилл", "Олеся","Николай","Филип"]

for y in range(0, len(students)):
    print(students[y])

word = "Test"
for s in word:
    print(s)

for student in students:
    print(student)

# напечатать не четные цифры
nums = (1,2,3,4,5,6,7,8,9,10)

for n in nums:
    if (n % 2 == 1):
        print(n)