list_of_books = []
while True:
    act = input("Выберите действие: добавить книгу, удалить книгу, изменить название, вывести индекс, остановить программу: ")
    if act == "добавить книгу":
        book = input("Введите название книги: ")
        list_of_books.append(book)
    elif act == "удалить книгу":
        book = input("Введите название книги: ")
        try:
            list_of_books.remove(book)
        except ValueError:
            print("Следи за списком книг")
    elif act == "изменить название":
        book = input("Введите название книги: ")
        try:
            book_index = list_of_books.index(book)
        except ValueError:
            print("Следи за списком книг: ")
            continue
        new_book = input("Введите новое название: ")
        list_of_books[book_index] = new_book
    elif act == "вывести индекс":
        book = input("Введите название книги: ")
        try:
            book_index = list_of_books.index(book)
        except ValueError:
            print("Следи за списком книг: ")
            continue
        print(f"Индекс: {book_index + 1}")
    else:
        break
