import json
import subprocess as sp

task_list_read = open('/home/arfors/.config/code/python-code/problem/json/task-list.json', 'r')
try:
  task_list = json.load(task_list_read)
except Exception as ex_:
  task_list_write = open('/home/arfors/.config/code/python-code/problem/json/task-list.json', 'w')
  task_list_write.write('{"":""}')
  task_list_write.close()
  task_list = json.loads(task_list_read.read())

def get_task_list():
  for i in task_list:
    print(i)
  
def last_id():
  task_list_keys = [i for i in task_list]
  try:
    return int(task_list_keys[-1][0])
  except Exception as ex_:
    return '2'

def new_task(task_name, task_description):
  task_list_write = open('/home/arfors/.config/code/python-code/problem/json/task-list.json', 'w')
  task_list[f'{last_id() + 1} - {task_name}'] = task_description
  json.dump(task_list, task_list_write)
  task_list_write.close()

def del_task(task_id):
  for i in task_list:
    if i[0] == task_id:
      del task_list[f'{i}']
      break
    
def execute_task(task_id):
  for i in task_list:
    if i[0] == task_id:
      sp.call(task_list.get(i), shell=True)

task_list_read.close()
