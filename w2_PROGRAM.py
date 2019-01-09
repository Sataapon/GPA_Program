def get_subjects(file_name):
    file = open(file_name)
    subjects = file.read().splitlines()
    file.close()
    return subjects

def save(subjects_studied, file_name):
    file = open(file_name, 'w')
    for item in subjects_studied:
        file.write(f'{item}\n')
    file.close

def insert(subjects_studied, new):
    subjects_studied.append(new)

def edit(subjects_studied, old, new):
    for i in range(len(subjects_studied)):
        if subjects_studied[i] == old:
            subjects_studied[i]= new

def check_command(cmd_arg):
    if cmd_arg[0] == 'open' and len(cmd_arg) == 2:
        return 'open'
    elif cmd_arg[0] == 'insert' and len(cmd_arg) == 2:
        return 'insert'
    elif cmd_arg[0] == 'edit' and len(cmd_arg) == 3:
        return 'edit'
    elif cmd_arg[0] == 'save' and len(cmd_arg) == 1:
        return 'save'
    elif cmd_arg[0] == 'exit' and len(cmd_arg) == 1:
        return 'exit'


subjects_studied = None
open_file = False
file_name = None

while True:
    cmd = input('Enter: ')
    cmd_arg = cmd.split(' ')

    in_command = check_command(cmd_arg)
    if in_command == 'open':
        subjects_studied = get_subjects(cmd_arg[1])
        open_file = True
        file_name = cmd_arg[1]
    elif in_command == 'save' and open_file:
        save(subjects_studied, file_name)
    elif in_command == 'insert' and open_file:
        insert(subjects_studied, cmd_arg[1])
    elif in_command == 'edit' and open_file:
        edit(subjects_studied, cmd_arg[1], cmd_arg[2])
    elif in_command == 'exit':
        break