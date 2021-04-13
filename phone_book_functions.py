def save_file(filename, content):
    try:
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(content)
    except FileExistsError:
        return 'not saved, file already exist'

    return 'file successfully saved'


def create_phone_book_json(filename):
    number_list = []
    entry = {'imie': 'Marta Nowak', 'numer': 500000000,
             'imie': 'Adam Kowalski', 'numer': 543567567}

    number_list.append(entry)
    number_list_json = json.dumps(number_list)

    save_file(filename, number_list_json)


def new_entry(phone_book_list):
    while True:
        user_input = input('Czy chcesz podać nowe dane do książki numerów? y/n: ')

        if user_input == 'y':
            new_entry_name = input('Podaj imię: ')

            while True:
                try:
                    new_entry_number = int(input('Podaj numer: '))
                except (ValueError):
                    print('To nie jest prawidłowa wartość! Spróbuj jeszcze raz!')
                    continue
                break

            new_entry = {'imie': new_entry_name, 'numer': new_entry_number}
            phone_book_list.append(new_entry)

        if user_input == 'n':
            return

        else:
            continue


def read_entry_list(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            print(f'Wczytano {len(list(data))} rekordów z książki telefonicznej. ')
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []

    return data


def save_new_data(data, filename):
    number_list_json = json.dumps(data)
    save_file(filename, number_list_json)


import json

if __name__ == "__main__":
    filename = 'phone_book.json'

    phone_book = read_entry_list(filename)
    new_entry(phone_book)
    save_new_data(phone_book, filename)