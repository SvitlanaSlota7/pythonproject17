from __future__ import annotations

class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books: list[Book] = []

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"

    def __repr__(self) -> str:
        return f"Author(name='{self.name}', country='{self.country}')"

class Book:
    # підрахунок всіх книг
    total_books_count: int = 0

    def __init__(self, name: str, year: int, author_obj: Author):
        self.name = name
        self.year = year
        self.author = author_obj
        Book.total_books_count += 1

    def __str__(self) -> str:
        return f"'{self.name}', {self.year}"

    def __repr__(self) -> str:
        return f"Book(name='{self.name}', year={self.year})"


class Library:
    def __init__(self, library_name: str):
        self.name = library_name
        self.books: list[Book] = []
        self.authors: list[Author] = []

    def new_book(self, book_name: str, year: int, author_inst: Author) -> Book:

        new_book_instance = Book(book_name, year, author_inst)
        self.books.append(new_book_instance)

        if author_inst not in self.authors:
            self.authors.append(author_inst)

        if new_book_instance not in author_inst.books:
            author_inst.books.append(new_book_instance)

        return new_book_instance

    def group_by_author(self, target_author: Author) -> list[Book]:
        return [b for b in self.books if b.author == target_author]

    def group_by_year(self, target_year: int) -> list[Book]:
        return [b for b in self.books if b.year == target_year]

    def __str__(self) -> str:
        return f"'{self.name}' ({len(self.books)} books)"


if __name__ == "__main__":
    my_library = Library("Global Wisdom Library")

    # Створюємо авторів
    ukrainian_author = Author("Serhiy Zhadan", "Ukraine", "1974-08-23")
    british_author = Author("J.K. Rowling", "UK", "1965-07-31")
    french_author = Author("Victor Hugo", "France", "1802-02-26")

    # Додаємо книги
    my_library.new_book("Voroshilovgrad", 2010, ukrainian_author)
    my_library.new_book("The Orphanage", 2017, ukrainian_author)
    my_library.new_book("Harry Potter", 1997, british_author)
    my_library.new_book("Les Misérables", 1862, french_author)

    print(f"{my_library}")

    print("\nAuthors list:")
    for auth in my_library.authors:
        print(f" {auth}")

    print("\nBooks list:")
    for bk in my_library.books:
        print(f" {bk} (Author: {bk.author.name})")

    print(f"\nBooks by {ukrainian_author.name}:")

    print(my_library.group_by_author(ukrainian_author))

    print(f"\nTotal books in system: {Book.total_books_count}")