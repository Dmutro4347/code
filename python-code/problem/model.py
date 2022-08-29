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
  pass

def new_task(task_name, task_description):
  task_list[f'{task_name}'] = task_description
  json.dump(task_list, task_list_write)

if __name__ == '__main__':
  new_task('test', 'test')