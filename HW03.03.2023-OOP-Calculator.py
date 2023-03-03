class Calculator:  # Создаем класс Calculator
    def __init__(self, a, c):  # Инициализируем конструктор
        self.a = a  # присваиваем динамические свойства
        self.c = c  # присваиваем динамические свойства

    def fplus(self):
        return self.a + self.c

    def fminus(self):
        return self.a - self.c

    def fmultiply(self):
        return self.a * self.c

    def fdividing(self):
        return self.a / self.c

    def fexponentiation(self):
        return self.a ** self.c


while ZeroDivisionError or Exception:  # зацикливаем программу, пока не введется кодовый символ (в нашем случае '0')
    try:
        print('*********************************************************************************')
        print('Программа "Калькулятор" ')
        print('Вводить необходимо только числа и знаки +, -, *, /, **.')
        print('При вводе "0" как первое значение или действие - означает "Выход из программы"')
        print('При вводе "0" как второе значение - означает "Ошибка! Деление на ноль!"')
        print('*********************************************************************************')
        a = input('Введите первое число:  ')
        if a == '0':  # создаем условие для выхода из программы через break
            print('Ноль. Программа завершена')
            break

        b = input('Введите действие:  ')
        if b == '0':  # создаем условие для выхода из программы через break
            print('Ноль. Программа завершена')
            break
        if b == '+' or b == '-' or b == '*' or b == '/' or b == '**':
            print('Действие:  ', b)

        c = input('Введите второе число:  ')
        if b == '/' and c == '0':  # создаем условие для действий при делении на ноль
            print('Деление на ноль!')
        elif b != '/' and c == '0':  # создаем условие для выхода из программы через break
            print('Ноль. Программа завершена')
            break

        a = float(a)
        c = float(c)

        calculator = Calculator(a, c)

        if b == '+':
            calculator.fplus()
            print('Сложение: ', a, '+', c, '=', calculator.fplus())
            print('Ответ:  ', calculator.fplus())

        elif b == '-':
            calculator.fminus()
            print('Вычитание: ', a, '-', c, '=', calculator.fminus())
            print('Ответ:  ', calculator.fminus())

        elif b == '*':
            calculator.fmultiply()
            print('Умножение: ', a, '*', c, '=', calculator.fmultiply())
            print('Ответ:  ', calculator.fmultiply())

        elif b == '/':
            calculator.fdividing()
            print('Деление: ', a, '/', c, '=', calculator.fdividing())
            print('Ответ:  ', calculator.fdividing())

        elif b == '**':
            calculator.fexponentiation()
            print('Возведение в степень: ', a, '**', c, '=', calculator.fexponentiation())
            print('Ответ:  ', calculator.fexponentiation())


    except ZeroDivisionError:
        print('Ошибка! Деление на ноль! Заново запустите программу и сделайте корректный ввод значений! ')  # исключаем
        # вывод ошибки "Деление на ноль"
        break
    except Exception:
        print('Некорректный ввод значений или команд. Вводить необходимо только числа и знаки +, -, *, /, ** . '
              'Сделайте корректный ввод значений и команд.')
        # исключаем вывод ошибки, в случае ввода текста

    else:
        print('*********************************************************************************')
        print('Вводить необходимо только числа и знаки +, -, *, /, ** ')
