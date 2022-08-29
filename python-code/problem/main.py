import view
import model

menu = view.View()
answer = menu.main_menu()

if answer == '1':
  model.get_task_list()
  answer = menu.task_menu()
  model.execute_task(answer)

elif answer == '2':
  answer = menu.new_task_menu()
  model.new_task(answer[0], answer[1])

elif answer == '3':
  pass

elif answer == '4':
  pass