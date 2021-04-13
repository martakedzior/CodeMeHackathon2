def save_file(filename, content):
    try:
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(content)
    except FileExistsError:
        return 'not saved, file already exist'

    return 'file successfully saved'


import json


if __name__ == "__main__":

    lista_numerow = []

    wpis = {
        'Anna Kowalska': 600000000,
        'Marta Kedzior': 500000000,
        'Marcin Grabowski': 501000000
    }

    lista_numerow.append(wpis)

    lista_numerow_json = json.dumps(lista_numerow)

    filename = 'ksiazka_numerow.json'

    save_file(filename, lista_numerow_json)