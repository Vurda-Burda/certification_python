import function as f
import ui

# Выбор действий
def run():
    input_from_user = ''
    ui.menu()
    input_from_user = input(' ').strip()
    # Показать заметки
    if input_from_user == '1':
        f.show('all')
        run()
    # Добавить заметку
    if input_from_user == '2':
        f.add()
        run()
    # Удалить заметку
    if input_from_user == '3':
        f.show('all')
        f.id_edit_del_show('del')
        run()
    # Редактировать заметку
    if input_from_user == '4':
        f.show('all')
        f.id_edit_del_show('edit')
        run()
    # Показать заметки по дате
    if input_from_user == '5':
        f.show('date')
        run()
    # Показать заметку по id
    if input_from_user == '6':
        f.show('id')
        f.id_edit_del_show('show')
        run()
    # Выход
    if input_from_user == '7':
        ui.goodbye()