from colorama import Fore

# def selectAction_value(string1, string2):
#     x = 0
#     while True:
#         try:
#             x = int(input(Fore.LIGHTBLUE_EX + f'{string1}'))
#             if x < 8 and x > 0:
#                 break
#             else:
#                 print(f'Введено некорректное значение {string2}\n')
#         except ValueError:
#                 print(f'введено некорректное значение. {string2}\n')
#     return x

def selectAction_value(string1, string2):
    try:
        x = int(input(Fore.LIGHTBLUE_EX + f'{string1}'))
        if x < 8 and x > 0:
            return x
        else:
            print(f'Введено некорректное значение {string2}\n')
            selectAction_value(string1, string2)
    except ValueError:
        print(f'введено некорректное значение. {string2}\n')
        selectAction_value(string1, string2)


def tryExceptInt(string):
    x = 0
    while True:
        try:
            x = int(input(Fore.LIGHTBLUE_EX + f'{string}'))
            break
        except ValueError:
            print(Fore.LIGHTBLUE_EX + 'Введено некорректное значение')
    return x