class Book:
    def __init__(self, name: str, author:str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages


book1 = Book("My_book", "Me", 200)
book2 = Book("Your_book", "You", 300)
