def set_subjects(file_name):
    try:
        file = open(file_name)
        subjects = file.read().splitlines()
        file.close()
        return subjects
    except FileNotFoundError:
        return None

def show_subjects(subjects):
    for i in subjects:
        print(i)

def convert_grade(value):
    if value == 'A': return 4
    elif value == 'B+': return 3.5
    elif value == 'B': return 3
    elif value == 'C+': return 2.5
    elif value == 'C': return 2
    elif value == 'D+': return 1.5
    elif value == 'D': return 1
    else: return 0

def calculate_GPA(subjects):
    sum_weight, sum = 0, 0
    for i in subjects:
        subject = i.split(',')
        sum_weight += int(subject[2])
        sum += int(subject[2]) * convert_grade(subject[3])
    return sum / sum_weight

def show_GPA(gpa):
    print(f'GPA = {gpa}')

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
    elif cmd_arg[0] == 'show'  and len(cmd_arg) == 1:
        return 'show'
    elif cmd_arg[0] == 'calculate' and len(cmd_arg) == 1:
        return 'calculate'
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
        if subjects:
            file_name = cmd_arg[1]
        else:
            file_name = None
    elif in_command == 'insert' and subjects:
        insert(subjects, cmd_arg[1])
    elif in_command == 'edit' and subjects:
        edit(subjects, cmd_arg[1], cmd_arg[2])
    elif in_command == 'show' and subjects:
        show_subjects(subjects)
    elif in_command == 'calculate' and subjects:
        gpa = calculate_GPA(subjects)
        show_GPA(gpa)
    elif in_command == 'save' and file_name:
        save(subjects, file_name)
    elif in_command == 'exit':
        break