def set_subjects(file_name):
    file = open(file_name)
    subjects = file.read().splitlines()
    file.close()
    return subjects

def save(subjects, file_name):
    file = open(file_name, 'w')
    for item in subjects:
        file.write(f'{item}\n')
    file.close

def insert(subjects, new):
    subjects.append(new)

def edit(subjects, old, new):
    for i in range(len(subjects)):
        if subjects[i] == old:
            subjects[i]= new

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

#--------------------------------------------------#

subjects = None
file_name = None

while True:
    cmd = input('Enter: ')
    cmd_arg = cmd.split(' ')

    in_command = check_command(cmd_arg)
    if in_command == 'open':
        subjects = set_subjects(cmd_arg[1])
        file_name = cmd_arg[1]
    elif in_command == 'save' and file_name:
        save(subjects, file_name)
    elif in_command == 'insert' and subjects:
        insert(subjects, cmd_arg[1])
    elif in_command == 'edit' and subjects:
        edit(subjects, cmd_arg[1], cmd_arg[2])
    elif in_command == 'exit':
        break