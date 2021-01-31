from utlis import database

user_choice = """
'a' = to add a new book
'l' = to list all books
'r' = to mark a book as read
'd' = to delete a book
'q' = to quit

your choice: """

def menu ():
    user_input = input(user_choice)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            pass
        elif user_input == 'r':
            pass
        elif user_input == 'd':
            pass
        elif user_input == 'q':
            pass
        else:
            print("please try again later")

        user_input = input(user_choice)

def prompt_add_book():
    book_name = input("Enter the book name: ")
    book_author = input("Enter the book author:  ")
    database.add_book(book_name, book_author)

def list_books():
    books = database.get_all_books()
    for book in books:
        print(book)
def prompt_read_book():
    book_name = input('Enter the book name you just finished reading')
    database.mark_book_read(book_name)
