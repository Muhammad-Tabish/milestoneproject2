from typing import List, Dict, Union
from .database_connection import Databaseconnection

"""
[
{
'name': 'tab',
'author': 'ham',
'read': True
}
]
"""


Book = Dict[str, Union[str, int]]
def create_book_table() -> None:
        with Databaseconnection ('data.db') as connection:
          cursor = connection.cursor()

          cursor.execute('CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer)')


def add_book(name: str, author) -> None:
    with Databaseconnection ('data.db') as connection:
       cursor = connection.cursor()

       cursor.execute('INSERT INTO books VALUES (?, ?, 0)', (name,author))

def get_all_books() -> List[Book]:
    with Databaseconnection ('data.db') as connection:
      cursor = connection.cursor()
      cursor.execute('SELECT * FROM books')
      books = [{'name': row[0],'author': row[1], 'read': row[2]}for row in cursor.fetchall()]

    return books

def mark_book_read(name : str) -> None:
   with Databaseconnection ('data.db') as connection:
      cursor = connection.cursor()

      cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))






def delete_book(name : str)-> None:
    with Databaseconnection ('data.db') as connection:
       cursor = connection.cursor()
       cursor.execute('DELETE FROM books WHERE name=?', (name,))



