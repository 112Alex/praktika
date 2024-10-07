from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import init
init()
from colorama import Fore, Back, Style

from functions import *
from tryExcept import *

init(autoreset=True)

exit = True
students = {"Antonio": (18, '21 ИС', {'математика': [2, 5], 'литература': [4, 4]})} # {name: (age, group {предмет: оценка)}

while exit:

    print(Fore.RED + '1.', end=' ')
    print('Добавить студента')
    print(Fore.RED + '2.', end=' ')
    print('Добавить оценки студенту (непрерывный ввод)')
    print(Fore.RED + '3.', end=' ')
    print('Вывести всех студентов')
    print(Fore.RED + '4.', end=' ')
    print('Найти студента по имени')
    print(Fore.RED + '5.', end=' ')
    print('Вывести студентов с баллом выше среднего')
    print(Fore.RED + '6.', end=' ')
    print('Вывести средние баллы по предметам')
    print(Fore.RED + '7.', end=' ')
    print('Выход\n')

    action = selectAction_value('Выбирите действие: ', 'Пожалуйста, введите число (от 1 до 7)')

    match action:
        case 1:
            students = {**students, **addStudent(students)} # {name: (age, group {предмет: оценка)}
            print(students)
        case 2:
            add_grades_continuously(students)
            print(students)
        case 3:
            showStudents(students)
        case 4:
            studentSearch(students)
        case 5:
            ...
        case 6:
            ...
        case 7:
            exit = False
        case _:
            print('z')





