a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if b == 0:
    raise ZeroDivisionError("Деление на ноль")

sum_result = a + b
difference = a - b
product = a * b
quotient = a / b
floor_division = a // b
remainder = a % b
power = a ** b

print(f"Сумма: {sum_result}")
print(f"Разность: {difference}")
print(f"Произведение: {product}")
print(f"Частное: {quotient}")
print(f"Целочисленное деление: {floor_division}")
print(f"Остаток от деления: {remainder}")
print(f"Возведение в степень: {power}")