
class Category:

    def __int__(self, name):
        self.name = name
        self.sub_category = list()
        self.books = list()

    def __str__(self):
        return "name: {0}, sub_category: {1}, books: {2}".\
            format(self.name, [i.__str__() for i in self.sub_category], [i.__str__() for i in self.books])
