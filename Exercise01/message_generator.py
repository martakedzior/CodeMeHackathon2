def save_file(filename, content):
    try:
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(content)
    except FileExistsError:
        return 'not saved, file already exist'
    return 'file successfully saved'


def read_file(filename):
    try:
        with open(filename) as file:
            text = file.read()
    except FileNotFoundError:
        return 'file not found error'

    if text == '':
        return 'file is empty'

    return text


def creating_data_structure(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        name_surname = []
        exercise = []
        grade_list = []
        student_class_li = []

        for row in csvreader:
            name = row[1] + " " + row[2]
            task = row[3]
            grade = row[4]
            if grade.isdigit() == False:
                grade = 0

            student_class = row[0]

            name_surname.append(name)
            exercise.append(task)
            grade_list.append(grade)
            student_class_li.append(student_class)

    return name_surname, exercise, grade_list, student_class_li


def creating_emails(name_surname, exercise, grade_list, student_class_li):
    message = read_file('message.txt')
    due_date = '30 June 2021'

    for i in range(0,len(name_surname)-1):
        message_to_save = message.format(name_surname[i],  student_class_li[i], exercise[i], grade_list[i], int(grade_list[i]) + 1, due_date)
        filename = 'email_to_' + name_surname[i] + ".txt"
        save_file(filename, message_to_save)
        i += 1


import csv

if __name__ == "__main__":

    filename = 'students.csv'

    try:
        name_surname, exercise, grade_list, student_class_li = creating_data_structure(filename)
        creating_emails(name_surname, exercise, grade_list, student_class_li)
    except FileExistsError:
        print('File not found')
