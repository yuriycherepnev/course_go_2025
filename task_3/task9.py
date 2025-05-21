A = float(input("Введите коэффициент A (A ≠ 0): "))
B = float(input("Введите коэффициент B: "))

if A != 0:
    x = -B / A
    print(f"x = {x}")
else:
    print("Коэффициент A не может быть равен 0")