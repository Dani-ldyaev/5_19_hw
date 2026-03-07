choice = int(input('Что вы хотите сделать? 1 - Разность, 2 - Деление: '))
x = int(input('x: '))

y = int(input('y: '))

if choice == 1:
    print(x-y)
elif choice == 2:
    print(x/y)
