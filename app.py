from utlis import database

user_choice = """
        WELCOME TO BOOK STORE
'a' = to add a new book
'l' = to list all books
'r' = to mark a book as read
'd' = to delete a book
'q' = to quit

your choice: """

def menu ():
    database.create_book_table()
    user_input = input(user_choice)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        elif user_input == 'q':
            pass
        else:
            print("please try again later")

        user_input = input(user_choice)

def prompt_add_book():
    name = input("Enter the book name: ")
    author = input("Enter the book author:  ")
    database.add_book(name, author)

def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'yes' if book['read'] else 'no'
        print(f"{book ['name']} by {book['author']}, read: {read}")
def prompt_read_book():
    name = input('Enter the book name you just finished reading: ')
    database.mark_book_read(name)

def prompt_delete_book():
    name = input("Enter the book name you wish to delete:  ")
    database.delete_book(name)

menu()