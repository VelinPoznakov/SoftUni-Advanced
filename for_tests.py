matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


x = 3
y = 3

for i in range(x * y):
    print(matrix[i // y][i % y])


class Book:
    def __init__(self, title):
        self.title = title
        self.books = []

    def add_book(self, title):
        if title not in self.books:
            return self.books.append(title)

        return f'{title} is already in the Library'

    def find_book(self, title):
        if title in self.books:
            return self.books[title]

        return 'Book not found'




