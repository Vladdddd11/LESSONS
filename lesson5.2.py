# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення -
# якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.
from unittest import case

while True:

    number1 = float(input("Введите первое число: "))
    number2 = float(input("Введите второе число: "))
    action = input("Введите действие(+, -, *, /): ")

    match action:
        case "+":
            print(number1 + number2)
        case "-":
            print(number1 - number2)
        case "*":
             print(number1 * number2)
        case "/" if number2 !=0:
             print(number1 / number2)
        case _:
             print("Некорректные действия")

    request = input("Продолжать вычисление Y/N ").upper()
    if request == "N":

        break
