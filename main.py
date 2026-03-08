from number_class import Number
import numpy as np
import config

print(config.APP_NAME)

choice = int(input('Что вы хотите сделать? 1 - Разность, 2 - Деление, 3 - Сложение, 4 - Умножение, 5 - Квадратный корень: '))

while True:
    x = Number(input("x: "))
    if not(x.getNumber() is None):
        break;

while True:
    y = Number(input("y: "))
    if not(x.getNumber() is None):
        break;

match choice:
    case 1:
        print(x.getNumber() - y.getNumber())
    case 2:
        print(x.getNumber() / y.getNumber())
    case 3:
        print(x.getNumber() + y.getNumber())
    case 4:
        print(x.getNumber() * y.getNumber())
    case 5:
        print(np.sqrt(x.getNumber()), np.sqrt(y.getNumber()))