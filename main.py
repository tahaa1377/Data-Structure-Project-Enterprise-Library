from max_heap import HeapArray
from category import Category
from book import Book


def add_a_new_category(newCategory):
    category1 = Category()
    category1.__int__(newCategory)
    main_list.append(category1)

def find_category_or_sub_category(main_list,new_sub_category):
    print("********************")

    for item in main_list:
        print(item)
        for i in item.sub_category:
            print(i)

    print("********************")


def add_a_subcategory_to_a_category(new_sub_category, category,main_list):

    for item in main_list:
        if item.name == category:
            category1 = Category()
            category1.__int__(new_sub_category)
            item.sub_category.append(category1)
            return True
        else:
            add_a_subcategory_to_a_category(new_sub_category, category, item.sub_category)

def add_a_book_to_a_category(book_to_a_category, author_name, price, category, main_list):

    for item in main_list:
        if item.name == category:
            book1 = Book()
            book1.__int__(book_to_a_category, author_name, price)
            item.books.append(book1)
            book_list.append(book1)
            return True
        else:
            add_a_book_to_a_category(book_to_a_category, author_name, price, category, item.sub_category)


def removing_a_book_from_category(book, category, main_list):

    for item in main_list:
        if item.name == category:
            for j, jtem in enumerate(item.books):
                if jtem.book_name == book:
                    del item.books[j]
                    book_list.remove(jtem)
                    return True
        else:
            removing_a_book_from_category(book, category, item.sub_category)


def delete_a_category_and_its_sub_categories_if_exist(delete_category, main_list):

    for i, item in enumerate(main_list):
        if item.name == delete_category:
            del main_list[i]
            return True
        else:
            delete_a_category_and_its_sub_categories_if_exist(delete_category, item.sub_category)

def print_tree():
    print("------------------")
    for i in main_list:
        print(i)
    print("------------------")


def search_book_name(book_name):

    for item in book_list:
        if item.book_name == book_name:
            return item


def book_lists():

    for item in book_list:
        print(item)


def list_books_from_category_name(category, main_list):

    for item in main_list:
        if item.name == category:
            print([i.__str__() for i in item.books])
            return True
        else:
            list_books_from_category_name(category, item.sub_category)


def order_book_name(book_name):

    for item in book_list:
        if item.book_name == book_name:
            order_book.append(item)
            print("added")
            break


def list_orders():
    return sorted(order_book, key=lambda x: x.price)


if __name__ == '__main__':
    print("data structure library project")

    maxheap = HeapArray()
    main_list = list()
    book_list = list()
    order_book = list()
    add_a_new_category("root")


    while True:
        print("1- Add a new category to the tree ")
        print("2- Add a subcategory to a category")
        print("3- Add a book to a category")
        print("4- Removing a book from the category")
        print("5- Delete a category and its sub-categories if exist")
        print("--")
        print("6- search book name")
        print("7- list books")
        print("8- list books from category name")
        print("9- order book name")
        print("10- list orders")
        print("----------------------------")
        n = int(input("select 1 - 10 : "))

        if n == 1:
            new_category = input("enter name of category : ")
            add_a_subcategory_to_a_category(new_category, "root", main_list)

        elif n == 2:
            new_sub_category = input("enter name of sub category : ")
            category = input("enter name of category : ")
            add_a_subcategory_to_a_category(new_sub_category, category, main_list)

        elif n == 3:
            book_name = input("enter book to a category : ")
            author_name = input("enter author book name : ")
            price = int(input("enter price book : "))
            category = input("enter book to a category : ")
            add_a_book_to_a_category(book_name, author_name, price, category, main_list)


        elif n == 4:
            book = input("enter book to remove: ")
            category = input("enter name of category : ")
            removing_a_book_from_category(book, category, main_list)

        elif n == 5:
            delete_category = input("enter category to remove: ")
            delete_a_category_and_its_sub_categories_if_exist(delete_category, main_list)

        elif n == 6:
            book_name = input("enter book name: ")
            print(search_book_name(book_name))

        elif n == 7:
            book_lists()

        elif n == 8:
            category = input("enter category : ")
            list_books_from_category_name(category, main_list)

        elif n == 9:
            book_name = input("enter book name : ")
            order_book_name(book_name)

        elif n == 10:

           for i in list_orders():
               print(i.__str__())


        print_tree()
        # find_category_or_sub_category(main_list)




