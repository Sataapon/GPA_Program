import re

#--------------------------------------------------#

class Subject():
    """
    Store code, name, weight and grade for subject
    """
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
    """
    Create subject from string
    """
    subject = in_subject.split(',')
    return Subject(subject[0], subject[1], subject[2], subject[3])

#--------------------------------------------------#

def set_subjects(file_name):
    """
    Create list of all subjects
    """
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

def have_subject(subjects, in_subject):
    """
    Check subject already in list
    """
    for subject in subjects:
        if subject.code == in_subject.code:
            return True
        elif subject.name == in_subject.name:
            return True
    return False

#--------------------------------------------------#

def valid_subject(subject):
    """
    Check pattern of subject
    """
    subject_pattern = re.compile(r'0\d{8},[A-Z](([A-Z]| ){1,28}[A-Z]|[A-Z]?),[1-3],([A-D][+]?|F)')
    return re.fullmatch(subject_pattern, subject)

#--------------------------------------------------#

def insert_subject(subjects, subject_new):
    """
    Insert subject to list
    """
    subjects.append(subject_new)

#--------------------------------------------------#

def edit_subject(subjects, subject_old, subject_new):
    """
    Edit subject in list
    """
    for i in range(len(subjects)):
        if subjects[i] == subject_old:
            subjects[i] = subject_new
            return

#--------------------------------------------------#

def delete_subject(subjects, subject_old):
    """
    Delete subject from list
    """
    for i in range(len(subjects)):
        if subjects[i] == subject_old:
            subjects.remove(subjects[i])
            return

#--------------------------------------------------#

def save_subjects(subjects, file_name):
    """
    Save all subjects
    """
    file = open(file_name, 'w')
    for subject in subjects:
        file.write(f'{subject.code},{subject.name},{subject.weight},{subject.grade}\n')
    file.close

#--------------------------------------------------#

def show_subjects(subjects):
    """
    Display all subjects
    """
    for subject in subjects:
        print(subject.code + ', ' + subject.name + ', ' + subject.weight + ', ' + subject.grade)

#--------------------------------------------------#

def convert_grade(grade):
    """
    Convert grade from symbol to number
    """
    grades = {'A': 4, 'B+' : 3.5, 'B': 3, 'C+': 2.5, 'C': 2, 'D+': 1.5, 'D': 1, 'F': 0}
    return grades[grade]

#--------------------------------------------------#

def calculate_GPA(subjects):
    """
    Calculate GPA from all subjects
    """
    sum_weight, sum = 0, 0
    for subject in subjects:
        sum_weight += int(subject.weight)
        sum += int(subject.weight) * convert_grade(subject.grade)
    return sum / sum_weight

#--------------------------------------------------#

def show_GPA(gpa):
    """
    Display GPA
    """
    print(f'GPA = {gpa}')

#--------------------------------------------------#

def check_command(cmd_arg):
    """
    Check correct command
    """
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

def split_input(cmd):
    """
    Seperate command
    """
    cmd_arg = []
    quote = False
    cmd_arg.append('')
    arg_index = 0
    for i in range(len(cmd)):
        if cmd[i] == "'":
            quote = not quote
        elif cmd[i] == ' ':
            if quote:
                cmd_arg[arg_index] += cmd[i]
            else:
                cmd_arg.append('')
                arg_index += 1
        else:
            cmd_arg[arg_index] += cmd[i]
    return cmd_arg

#--------------------------------------------------#

subjects = None
file_name = None

while True:
    cmd = input('Enter: ')
    cmd_arg = split_input(cmd)

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
