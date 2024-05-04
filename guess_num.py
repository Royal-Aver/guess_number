from random import randint

def guessing_game():
    random_num = randint(1, 30)

    num_attempts = 3

    print(f'Угадайте загаданное число от 1 до 30! У Вас есть {num_attempts} попыток')

    while num_attempts > 0:
        try:
            num_user = int(input('Введите Ваше число: '))
            if num_user > random_num:
                print(f'Ваше число больше! Осталось попыток {num_attempts - 1}!')
            elif num_user < random_num:
                print(f'Ваше число меньше! Осталось попыток {num_attempts - 1}')
            else:
                print(f'Вы угадали! Загаданное число - это {random_num}')
                break
        except ValueError:
            print('Можно вводить только целые числа')

        num_attempts -= 1


guessing_game()