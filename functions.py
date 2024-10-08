from colorama import Fore, Back, Style
from colorama import init
init()
init(autoreset=True)


from tryExcept import tryExceptInt


def addStudent(dict):
    name = input(Fore.LIGHTBLUE_EX + 'Введите фио студента: ')
    age = tryExceptInt('Введите возраст студента: ')
    group = input(Fore.LIGHTBLUE_EX + 'Введите группу студента: ')
    tup = (age, group, {})
    dict[f'{name}'] = tup
    return dict


def addGradesContinuously(students):
    print(Fore.CYAN + "Введите имя студента для добавления оценок (или 'стоп' для выхода):", end=' ')
    name = input()
    if name.lower() == "стоп":
        return

    if name not in students:
        print(Fore.RED + f"Студент с именем {name} не найден.\n")
        return

    print(Fore.CYAN + f"Добавление оценок для студента {name}. Введите 'стоп' в качестве предмета, чтобы завершить.")

    while True:
        print(Fore.CYAN + "Введите предмет (или 'стоп' для завершения):", end=' ')
        subject = input()
        if subject.lower() == "стоп":
            break

        try:
            print(Fore.CYAN + f"Введите оценку по предмету {subject} (от 2 до 5):", end=' ')
            grade = int(input())
            if grade < 2 or grade > 5:
                print(Fore.RED + "Ошибка: оценка должна быть в диапазоне от 2 до 5.")
                continue
        except ValueError:
            print(Fore.RED + "Ошибка: введите корректную числовую оценку.")
            continue

        # Добавление оценки в список оценок студента
        if subject in students[name][2]:
            students[name][2][subject].append(grade)
        else:
            students[name][2][subject] = [grade]

    print(Fore.LIGHTBLUE_EX + f"Оценки для студента {name} добавлены.\n")


def showStudents(students):
    for item in students:
        print(Fore.WHITE + f'{item}, Возраст: {students[item][0]}, Группа: {students[item][1]}', end=' ')
        for grade in students[item][2]:
            average = sum(students[item][2][grade]) / len(students[item][2][grade])
            print(Fore.CYAN + f'{grade}: ', (round(average, 2)))
        print()

def studentSearch(students):
    print(Fore.LIGHTBLUE_EX + 'Введите имя студента:', end=' ')
    item = input()
    result = students.get(item, (Fore.RED + 'студент не найден'))
    if result != (Fore.RED + 'студент не найден'):
        print(f'{item}, Возраст: {result[0]}, Группа: {result[1]}')
        for grade in students[item][2]:
            average = sum(students[item][2][grade]) / len(students[item][2][grade])
            print(Fore.CYAN + f'{grade}: ', (round(average, 2)))
    else:
        print(Fore.RED + 'Студент не найден!')

def showCoolStudents(students):
    req = tryExceptInt('Введите пороговое значение среднего балла: ')
    if req >= 1 and req <=5:
        n = 0
        for item in students:
            sumOfGrades = 0
            k = 0
            for grade in students[item][2]:
                for i in students[item][2][grade]:
                    k += 1
                    sumOfGrades += i
            if (sumOfGrades/k) > req:
                print(Fore.WHITE + item, end='\n\n')
                n += 1
        if n == 0:
            print(Fore.RED + 'подходящие студенты не найдены! \n')
    else:
        print(Fore.BLUE + 'Введено некорретное значение')
        showCoolStudents(students)


def showAvgGrades(students):
    sbjs = {} # {предмет: [оценка, оценка...]}

    for item in students:
        for subject in students[item][2]:
            sbjs.update({subject})
            for i in students[item][2][subject]:
                sbjs[subject].append(i)

    print(sbjs)
# TODO: дописать функцию







