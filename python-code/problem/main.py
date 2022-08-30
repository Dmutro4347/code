import view
import model

while True:

  menu = view.View()
  answer = menu.main_menu()

  if answer == '1':
    model.get_task_list()
    answer = menu.task_menu()
    model.execute_task(answer)
    continue

  elif answer == '2':
    answer = menu.new_task_menu()
    model.new_task(answer[0], answer[1])
    continue

  elif answer == '3':
    model.get_task_list()
    answer = menu.del_task_menu()
    model.del_task(answer)
    continue

  elif answer == '4':
    break