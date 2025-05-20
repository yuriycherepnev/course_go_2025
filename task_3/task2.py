# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"

age = int(age)
try:
    foo = int(foo)
except ValueError:
    foo = 0  # или другое значение по умолчанию
    print("Не удалось преобразовать foo в число")

print(f"age: {age}, {type(age)}")
print(f"foo: {foo}, {type(foo)}")

# Преобразуйте переменную age в Boolean
age = "123abc"
age = bool(age)

print(f"age: {age}, {type(age)}")

# Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag)

print(f"flag: {flag}, {type(flag)}")

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
str_one = bool(str_one)
str_two = bool(str_two)

print(f"str_one: {str_one}, {type(str_one)}")
print(f"str_two: {str_two}, {type(str_two)}")

# Преобразуйте значение 0 и 1 в Boolean
zero_bool = bool(0)  # False
one_bool = bool(1)   # True

print(f"zero_bool: {zero_bool}, {type(zero_bool)}")
print(f"one_bool: {one_bool}, {type(one_bool)}")

# Преобразуйте False в строку
false_str = str(False)  # "False"

print(f"false_str: {false_str}, {type(false_str)}")