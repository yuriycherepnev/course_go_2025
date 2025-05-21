number = int(input("Введите четырёхзначное число: "))

# Проверяем, что число четырёхзначное
if 1000 <= number <= 9999:
    digit1 = number // 1000          # Первая цифра
    digit2 = (number // 100) % 10    # Вторая цифра
    digit3 = (number // 10) % 10     # Третья цифра
    digit4 = number % 10             # Четвёртая цифра

    is_palindrome = (digit1 == digit4) and (digit2 == digit3)
    print(is_palindrome)
else:
    print("Ошибка: число должно быть четырёхзначным.")