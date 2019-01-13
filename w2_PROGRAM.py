import re

#--------------------------------------------------#

class Subject():
    def __init__(self, code, name, weight, grade):
        self.code = code
        self.name = name
        self.weight = weight
        self.grade = grade

    def __eq__(self, other):
        return self.code == other.code and self.name == other.name and \
            self.weight == other.weight and self.grade == other.grade

#--------------------------------------------------#

def create_subject(in_subject):
    subject = in_subject.split(',')
    return Subject(subject[0], subject[1], subject[2], subject[3])

#--------------------------------------------------#

def set_subjects(file_name):
    try:
        file = open(file_name)
        lines = file.read().splitlines()
        file.close()
        subjects = []
        for line in lines:
            subjects.append(create_subject(line))
        return subjects
    except FileNotFoundError:
        return None

#--------------------------------------------------#

def have_subject(subjects, subject):
    for i in subjects:
        if i.code == subject.code:
            return True
        elif i.name == subject.name:
            return True
    return False

#--------------------------------------------------#

def valid_subject(subject):
    subject_pattern = re.compile(r'0\d{8},[A-Z](([A-Z]| ){1,28}[A-Z]|[A-Z]?),[1-3],([A-D][+]?|F)')
    return re.fullmatch(subject_pattern, subject)

#--------------------------------------------------#

def insert_subject(subjects, subject_new):
    subjects.append(subject_new)

#--------------------------------------------------#

def edit_subject(subjects, subject_old, subject_new):
    for i in range(len(subjects)):
        if subjects[i] == subject_old:
            subjects[i] = subject_new
            return

#--------------------------------------------------#

def delete_subject(subjects, subject_old):
    for i in range(len(subjects)):
        if subjects[i] == subject_old:
            subjects.remove(subjects[i])
            return

#--------------------------------------------------#

def save_subjects(subjects, file_name):
    file = open(file_name, 'w')
    for subject in subjects:
        file.write(f'{subject.code},{subject.name},{subject.weight},{subject.grade}\n')
    file.close

#--------------------------------------------------#

def show_subjects(subjects):
    for i in subjects:
        print(i.code + ', ' + i.name + ', ' + i.weight + ', ' + i.grade)

#--------------------------------------------------#

def convert_grade(grade):
    grades = {'A': 4, 'B+' : 3.5, 'B': 3, 'C+': 2.5, 'C': 2, 'D+': 1.5, 'D': 1, 'F': 0}
    return grades[grade]

#--------------------------------------------------#

def calculate_GPA(subjects):
    sum_weight, sum = 0, 0
    for i in subjects:
        sum_weight += int(i.weight)
        sum += int(i.weight) * convert_grade(i.grade)
    return sum / sum_weight

#--------------------------------------------------#

def show_GPA(gpa):
    print(f'GPA = {gpa}')

#--------------------------------------------------#

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

"""
def split_input(cmd):
    cmd_arg = []
    i = 0
    cmd_arg.append('')
    for arg in cmd:
        if arg == ' ':
            cmd_arg.append('')
            i += 1
        else:
            cmd_arg[i] += arg
    return cmd_arg
"""

#--------------------------------------------------#

subjects = None
file_name = None

while True:
    cmd = input('Enter: ')
    cmd_arg = cmd.split(' ') # BUG when space in subject name

    in_command = check_command(cmd_arg)
    if in_command == 'open':
        subjects = set_subjects(cmd_arg[1])
        if subjects:
            file_name = cmd_arg[1]
        else:
            file_name = None
    elif in_command == 'insert' and subjects:
        if valid_subject(cmd_arg[1]):
            if not have_subject(subjects, create_subject(cmd_arg[1])):
                insert_subject(subjects, create_subject(cmd_arg[1]))
    elif in_command == 'edit' and subjects:
        if valid_subject(cmd_arg[1]) and valid_subject(cmd_arg[2]):
            temp_subjects = subjects[:]
            delete_subject(temp_subjects, create_subject(cmd_arg[1]))
            if not have_subject(temp_subjects, create_subject(cmd_arg[2])):
                edit_subject(subjects, create_subject(cmd_arg[1]), create_subject(cmd_arg[2]))
    elif in_command == 'delete' and subjects:
        if valid_subject((cmd_arg[1])):
            delete_subject(subjects, create_subject(cmd_arg[1]))
    elif in_command == 'save' and file_name:
        save_subjects(subjects, file_name)
    elif in_command == 'show' and subjects:
        show_subjects(subjects)
    elif in_command == 'gpa' and subjects:
        show_GPA(calculate_GPA(subjects))
    elif in_command == 'exit':
        break