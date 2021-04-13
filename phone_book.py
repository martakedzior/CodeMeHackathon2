from phone_book_functions import read_entry_list, new_entry, save_new_data


if __name__ == "__main__":

    filename = 'phone_book.json'

    phone_book = read_entry_list(filename)
    new_entry(phone_book)
    save_new_data(phone_book, filename)
