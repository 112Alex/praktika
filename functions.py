from colorama import Fore, Back, Style

from tryExcept import tryExceptInt


def addStudent(dict):
    name = input(Fore.BLUE + 'Введите фио студента: ')
    age = tryExceptInt('Введите возраст студента: ')
    group = input(Fore.BLUE + 'Введите группу студента: ')
    tup = (age, group, {})
    dict[f'{name}'] = tup
    return dict


# Функция для добавления оценок студенту по предмету (непрерывный ввод)
def add_grades_continuously(students):
    name = input("Введите имя студента для добавления оценок (или 'стоп' для выхода): ")
    if name.lower() == "стоп":
        return

    if name not in students:
        print(f"Студент с именем {name} не найден.")
        return

    print(f"Добавление оценок для студента {name}. Введите 'стоп' в качестве предмета, чтобы завершить.")

    while True:
        subject = input("Введите предмет (или 'стоп' для завершения): ")
        if subject.lower() == "стоп":
            break

        try:
            grade = int(input(f"Введите оценку по предмету {subject} (от 2 до 5): "))
            if grade < 2 or grade > 5:
                print("Ошибка: оценка должна быть в диапазоне от 2 до 5.")
                continue
        except ValueError:
            print("Ошибка: введите корректную числовую оценку.")
            continue

        # Добавление оценки в список оценок студента
        if subject in students[name][2]:
            students[name][2][subject].append(grade)
        else:
            students[name][2][subject] = [grade]

    print(f"Оценки для студента {name} добавлены.")


def showStudents(students):
    for item in students:
        print(f'{item}, Возраст: {students[item][0]}, Группа: {students[item][1]}')
        sred = 0
# Дописать функцию showStudents

def studentSearch(students):
    for grade in students[grade][2]:
        print(grade)
