import notepad

# Создание заметки
def create_note(number):
    title = check_len_text_input(
        input('Введите название заметки: '), number)
    body = check_len_text_input(
        input('Введите описание заметки: '), number)
    return notepad.Note(title=title, body=body)

# Меню программы
def menu():
    print("\n Заметки: \n \n 1 - вывод всех заметок \n 2 - добавление заметки \n 3 - удаление заметки \n 4 - редактирование заметки \n 5 - выборка заметок по дате \n 6 - показать заметку по id \n 7 - выход \n \n Введите номер: ")

# Проверка количества введенных символов
def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Повторите ввод: ')
    else:
        return text

# Выход
def goodbye():
    print(" Выполнен выход.")
