# Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
# яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба,
# мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters,
# з усім набором потрібних букв
# Приклад:
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

letters = input("Введите через дефис 2 буквы (a-c): ")
control = string.ascii_letters
first_letter =  letters[0]
second_letter = letters[2]

start_index = control.index(first_letter)
end_index = control.index(second_letter)

print(control[start_index:end_index+1])