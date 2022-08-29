import view
import model

menu = view.View()
answer = menu.main_menu()

if answer == '1':
  model.get_task_list()