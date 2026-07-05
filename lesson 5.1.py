# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної може містити символ _, але не може містити два символи __ підряд.
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))

import string
import keyword


name = input("Введите имя переменной: ")
examination = string.punctuation
is_valid = True

if name in keyword.kwlist:
    is_valid = False

if "__" in name:
    is_valid = False

for symbol in name:
    if symbol in examination and symbol != "_":
        is_valid = False
    if symbol == " ":
        is_valid = False
    if symbol.isupper():
        is_valid = False

if name == "":
    is_valid = False

if name != "" and name[0].isdigit():
    is_valid = False

print(is_valid)