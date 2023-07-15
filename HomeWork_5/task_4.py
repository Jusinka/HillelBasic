numbers = [5, 12, 7, 42, 8, 3, 10, 6, 9]
count = 0

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] = 0
        count += 1

print("Кількість замінених чисел:", count)
print("Список після заміни:", numbers)