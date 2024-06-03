import json
from pathlib import Path

class Book:
    """A class to represent a library catalog"""

    def __init__(self, title, author,genre, availability):
        """Initialize parameters of the book class"""
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = availability

    def add_books(self):

        self.book = {
            'Fiction':['Harry Potter', 'Alice In Wonderland','Cindrella'],
            'History': ['The Rise and fall of the Third Reich'],
            'Non-ficiton': ['Power','Twelve Rules for Life'],
            'Linguisitic': ['Teaching English to Middle schoolers']
            }
        # Convert python string to json file
        json_contents = json.dump(self.books)

        # define the path where to store the file and file's name
        file_path = Path("libaray_catalog.json")

        # Write json content to the file
        file_path.write_text(json_contents)


        for book in self.book.key():
            return book

    def search_books(self):
        pass

saturday = Book('nmn', 'jkjkl', 'juuu', 'fgfg')
