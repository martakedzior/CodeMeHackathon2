def save_file(filename, content):
    try:
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(content)
    except FileExistsError:
        return 'not saved, file already exist'

    return 'file successfully saved'


def new_entry(list):
    user_input = input('Czy chcesz podać nowe dane do książki numerów? y/n: ')

    new_entry = {
    }

    if user_input == 'y':
        new_entry_name = input('Podaj imię: ')

        while True:
            try:
                new_entry_number = int(input('Podaj numer: '))
            except (ValueError):
                print('To nie jest prawidłowa wartość! Spróbuj jeszcze raz!')
                continue
            break

        new_entry[new_entry_name] = new_entry_number
        list.append(new_entry)


def read_entry_list():
    filename = 'phone_book.json'

    with open(filename, 'r') as f:
        data = json.load(f)

    return data


import json

if __name__ == "__main__":
    number_list = []
    entry = {
        'Anna Kowalska': 600000000,
        'Marta Kedzior': 500000000,
        'Marcin Grabowski': 501000000
    }

    number_list.append(entry)
    number_list_json = json.dumps(number_list)
    filename = 'phone_book.json'

    save_file(filename, number_list_json)

    new_entry(number_list)
    number_list_json = json.dumps(number_list)
    save_file(filename, number_list_json)

    read_entry_list()