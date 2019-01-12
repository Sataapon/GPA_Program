import re

def set_subjects(file_name):
    try:
        file = open(file_name)
        subjects = file.read().splitlines()
        file.close()
        return subjects
    except FileNotFoundError:
        return None

def valid_subject(subject):
    subject_pattern = re.compile(r'0\d{8},[A-Z](([A-Z]| ){1,28}[A-Z]|[A]?),[1-3],([A-D][+]?|F)') #BUG when space in subject name
    print(subject)
    return re.fullmatch(subject_pattern, subject)

def insert(subjects, subject_new):
    subjects.append(subject_new)

def edit(subjects, subject_old, subject_new):
    for i in range(len(subjects)):
        if subjects[i] == subject_old:
            subjects[i]= subject_new

def delete(subjects, subject):
    subjects.remove(subject)

def save(subjects, file_name):
    file = open(file_name, 'w')
    for item in subjects:
        file.write(f'{item}\n')
    file.close

def show_subjects(subjects):
    for i in subjects:
        print(i)

def convert_grade(grade):
    grades = {'A': 4, 'B+' : 3.5, 'B': 3, 'C+': 2.5, 'C': 2, 'D+': 1.5, 'D': 1, 'F': 0}
    return grades[grade]

def calculate_GPA(subjects):
    sum_weight, sum = 0, 0
    for i in subjects:
        subject = i.split(',')
        sum_weight += int(subject[2])
        sum += int(subject[2]) * convert_grade(subject[3])
    return sum / sum_weight

def show_GPA(gpa):
    print(f'GPA = {gpa}')

def check_command(cmd_arg):
    if cmd_arg[0] == 'open' and len(cmd_arg) == 2:
        return 'open'
    elif cmd_arg[0] == 'insert' and len(cmd_arg) == 2:
        return 'insert'
    elif cmd_arg[0] == 'edit' and len(cmd_arg) == 3:
        return 'edit'
    elif cmd_arg[0] == 'delete' and len(cmd_arg) == 2:
        return 'delete'
    elif cmd_arg[0] == 'save' and len(cmd_arg) == 1:
        return 'save'
    elif cmd_arg[0] == 'show' and len(cmd_arg) == 1:
        return 'show'
    elif cmd_arg[0] == 'gpa' and len(cmd_arg) == 1:
        return 'gpa'
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
        if valid_subject(cmd_arg[1]):
            insert(subjects, cmd_arg[1])
    elif in_command == 'edit' and subjects:
        if valid_subject(cmd_arg[1]) and valid_subject(cmd_arg[2]):
            edit(subjects, cmd_arg[1], cmd_arg[2])
    elif in_command == 'delete' and subjects:
        delete(subjects, cmd_arg[1])
    elif in_command == 'save' and file_name:
        save(subjects, file_name)
    elif in_command == 'show' and subjects:
        show_subjects(subjects)
    elif in_command == 'gpa' and subjects:
        show_GPA(calculate_GPA(subjects))
    elif in_command == 'exit':
        break