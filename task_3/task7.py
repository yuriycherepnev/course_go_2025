A = float(input("Введите координату точки A: "))
B = float(input("Введите координату точки B: "))
C = float(input("Введите координату точки C: "))

# abs() - вычисляет абсолютное значение (модуль) числа на оси координат
AC = abs(C - A)
BC = abs(C - B)

# Вычисляем сумму длин
sum_lengths = AC + BC

# Выводим результаты
print(f"Длина отрезка AC: {AC}")
print(f"Длина отрезка BC: {BC}")
print(f"Сумма длин отрезков: {sum_lengths}")