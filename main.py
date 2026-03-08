import numpy as np
import config

print(config.APP_NAME)

choice = int(input('Что вы хотите сделать? 1 - Разность, 2 - Деление, 3 - Сложение, 4 - Умножение, 5 - Квадратный корень'))

x = int(input("x: "))

y = int(input("y: "))

match choice:
    case 1:
        print(x - y)
    case 2:
        print(x / y)
    case 3:
        print(x + y)
    case 4:
        print(x * y)
    case 5:
        print(np.sqrt(x), np.sqrt(y))

