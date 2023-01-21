
class Book:

    def __int__(self, book_name, author_name, price):
        self.book_name = book_name
        self.author_name = author_name
        self.price = price

    def __str__(self):
        return "book_name: {0}, author_name: {1}, price: {2}".format(self.book_name, self.author_name, self.price)
