books = []

def add_book(name, author):
    books.append({"name" : name, "author": author, 'read': False})

def get_all_books():
    return books

def mark_book_read(book_name):
    for book in books:
        if book ['name'] == book_name:
            book['read'] == True
