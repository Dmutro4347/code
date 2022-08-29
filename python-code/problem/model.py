import json

task_list_read = open('/home/arfors/.config/code/python-code/problem/json/task-list.json', 'r')
try:
  task_list = json.loads(task_list_read.read())
except Exception as ex_:
  task_list_write = open('/home/arfors/.config/code/python-code/problem/json/task-list.json', 'w')
  task_list_write.write('{}')
  task_list = json.loads(task_list_read.read())

  
task_list_write = open('/home/arfors/.config/code/python-code/problem/json/task-list.json', 'w')

def get_task_list():
  for i in task_list:
    print(i)
  
def last_id():
  task_list_keys = [i for i in task_list]
  return int(task_list_keys[-1][0])

def new_task(task_name, task_description):
  task_list[f'{last_id() + 1} - {task_name}'] = task_description
  json.dump(task_list, task_list_write)

def execute_task(task_id):
  for i in task_list:
    if task_list[0] == task_id:
      print(task_list.get(i))

if __name__ == '__main__':
  execute_task('2')