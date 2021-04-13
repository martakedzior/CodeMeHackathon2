def save_file(filename, content):
    try:
        with open(filename, 'x', encoding='UTF-8') as file:
            file.write(content)
    except FileExistsError:
        return 'not saved, file already exist'
    return 'file successfully saved'


def read_file(filename):
    text = '***'
    try:
        with open(filename) as file:
            text = file.read()
    except FileNotFoundError:
        return 'file not found error'

    if text == '':
        return 'file is empty'

    return text


def creating_messages(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        for row in csvreader:
            message = read_file('message.txt')
            name = row[1] + " " + row[2]
            task = row[3]
            grade = row[4]
            student_class = row[0]
            due_date = '30 June 2021'

            message = message.format(name, student_class, task, grade, int(grade) + 1, due_date)

            filename = 'email_to_' + row[1] + "_" + row[2] + ".txt"
            save_file(filename, message)


import csv

if __name__ == "__main__":

    filename = 'students.csv'

    try:
        creating_messages(filename)
    except FileExistsError:
        print('file not found')