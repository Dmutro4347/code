class View:

  def main_menu(self):
    print('1 - Список задач')
    print('2 - Додати задачу')
    print('3 - Видалити задачу')
    print('4 - Вихід')


    return input('Що робимо? ')

  def new_task_menu(self):
    return (
      input("Ім'я задачі: "),
      input('Опис задачі: ')
    )
  
  def task_menu(self):
    return input(':> ')

  def del_task_menu(self):
    return input('Що видаляти? ')