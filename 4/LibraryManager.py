class LibraryManager:
    def __init__(self):
        self.library = {}

    def add_book(self, isbn, title, author, publisher, volume, year):
        if isbn in self.library:
            print(f"Book with ISBN {isbn} already exists in the library.")
            return
        self.library[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year': year
        }
        print(f"Book '{title}' added to the library.")

    def remove_book(self, isbn):
        if isbn in self.library:
            del self.library[isbn]
            print(f"Book with ISBN {isbn} removed from the library.")
        else:
            print(f"Book with ISBN {isbn} not found in the library.")

    def retrieve_book(self, isbn):
        if isbn in self.library:
            return self.library[isbn]
        else:
            print(f"Book with ISBN {isbn} not found in the library.")
            return None

    def search_books(self, title=None, author=None):
        results = []
        for book in self.library.values():
            if (title and title.lower() in book['title'].lower()) or (author and author.lower() in book['author'].lower()):
                results.append(book)
        return results

    def list_books(self):
        return list(self.library.values())

    def update_book(self, isbn, **kwargs):
        if isbn in self.library:
            for key, value in kwargs.items():
                if key in self.library[isbn]:
                    self.library[isbn][key] = value
            print(f"Book with ISBN {isbn} updated.")
        else:
            print(f"Book with ISBN {isbn} not found in the library.")

    def check_availability(self, isbn):
        return isbn in self.library


sample_books = [
    ("978-0134670959", "Operating System Concepts", "Abraham Silberschatz", "Wiley", 10, 2020),
    ("978-0133591629", "Modern Operating Systems", "Andrew S. Tanenbaum", "Pearson", 4, 2020),
    ("978-0262044690", "Structure and Interpretation of Computer Programs", "Harold Abelson", "MIT Press", 2, 2020),
    ("978-0134093413", "Data Structures and Algorithm Analysis in C++", "Mark Allen Weiss", "Pearson", 4, 2021),
    ("978-0134853987", "Artificial Intelligence: A Modern Approach", "Stuart Russell", "Pearson", 4, 2021),
    ("978-0134685991", "Clean Code", "Robert C. Martin", "Pearson", 1, 2021),
    ("978-0132350884", "Agile Software Development, Principles, Patterns, and Practices", "Robert C. Martin", "Pearson", 1, 2020),
    ("978-0134757599", "Refactoring: Improving the Design of Existing Code", "Martin Fowler", "Pearson", 2, 2020),
    ("978-0134092676", "Introduction to the Theory of Computation", "Michael Sipser", "Cengage Learning", 3, 2021),
    ("978-0262033847", "Introduction to Algorithms", "Thomas H. Cormen", "MIT Press", 3, 2022),
    ("978-0132149178", "Design Patterns: Elements of Reusable Object-Oriented Software", "Erich Gamma", "Pearson", 1, 2021),
    ("978-0134787962", "Effective Java", "Joshua Bloch", "Pearson", 3, 2021),
    ("978-0201633610", "The Mythical Man-Month: Essays on Software Engineering", "Frederick P. Brooks Jr.", "Addison-Wesley", 2, 2020),
    ("978-0135159941", "The Pragmatic Programmer", "Andrew Hunt", "Addison-Wesley", 2, 2021),
    ("978-1492077213", "Designing Data-Intensive Applications", "Martin Kleppmann", "O'Reilly Media", 1, 2021),
    ("978-1492041139", "Python Data Science Handbook", "Jake VanderPlas", "O'Reilly Media", 1, 2020),
    ("978-0135172483", "Artificial Intelligence: Foundations of Computational Agents", "David L. Poole", "Cambridge University Press", 2, 2020),
    ("978-0321573513", "Computer Networking: A Top-Down Approach", "James F. Kurose", "Pearson", 6, 2020),
    ("978-1617294136", "Deep Learning with Python", "Francois Chollet", "Manning Publications", 1, 2020),
    ("978-1108445144", "Deep Learning", "Ian Goodfellow", "MIT Press", 1, 2020),
    ("978-1491987650", "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Aurélien Géron", "O'Reilly Media", 2, 2020),
    ("978-1484230069", "Python Machine Learning By Example", "Yuxi (Hayden) Liu", "Apress", 2, 2020),
    ("978-0128013528", "Machine Learning: A Probabilistic Perspective", "Kevin P. Murphy", "MIT Press", 1, 2022),
    ("978-1492041009", "Fluent Python", "Luciano Ramalho", "O'Reilly Media", 2, 2020),
    ("978-0134093413", "Data Structures and Algorithms in Python", "Michael T. Goodrich", "Wiley", 1, 2020)
]

if __name__ == "__main__":
    manager = LibraryManager()

    for isbn, title, author, publisher, volume, year in sample_books:
        manager.add_book(isbn, title, author, publisher, volume, year)

    print("\nAll books in the library:")
    print(manager.list_books())

    isbn_to_retrieve = "978-0134670959"
    print(f"\nRetrieving book with ISBN {isbn_to_retrieve}:")
    print(manager.retrieve_book(isbn_to_retrieve))

    isbn_to_remove = "978-0134670959"
    print(f"\nRemoving book with ISBN {isbn_to_remove}:")
    manager.remove_book(isbn_to_remove)
    print(f"\nChecking availability of book with ISBN {isbn_to_remove}:")
    print(manager.check_availability(isbn_to_remove))

    search_title = "Data Structures"
    print(f"\nSearching for books with title '{search_title}':")
    print(manager.search_books(title=search_title))

    isbn_to_update = "978-0133591629"
    print(f"\nUpdating book with ISBN {isbn_to_update}:")
    manager.update_book(isbn_to_update, author="Andrew Tanenbaum")
    print(manager.retrieve_book(isbn_to_update))

    print("\nAll books in the library after updates:")
    print(manager.list_books())

'''
Original dictionaries:
dict1: {'a': 1, 'b': 2, 'c': 3}
dict2: {'b': 2, 'c': 4, 'd': 5}
dict3: {'c': 3, 'd': 5, 'e': 6}

Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 6}

Common keys: {'c'}

Inverted dictionary (dict1): {1: 'a', 2: 'b', 3: 'c'}

Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 6}

Common keys: {'c'}

Inverted dictionary (dict1): {1: 'a', 2: 'b', 3: 'c'}

Inverted merged dictionary: {1: 'a', 2: 'b', 3: 'c', 5: 'd', 6: 'e'}
PS D:\MCA\python\lab2\3>


Common keys: {'c'}

Inverted dictionary (dict1): {1: 'a', 2: 'b', 3: 'c'}

Inverted merged dictionary: {1: 'a', 2: 'b', 3: 'c', 5: 'd', 6: 'e'}
PS D:\MCA\python\lab2\3> cd ..
PS D:\MCA\python\lab2> cd 4
PS D:\MCA\python\lab2\4> python LibraryManager.py     
Book 'Operating System Concepts' added to the library.
Book 'Modern Operating Systems' added to the library.
Book 'Structure and Interpretation of Computer Programs' added to the library.
Book 'Data Structures and Algorithm Analysis in C++' added to the library.
Book 'Artificial Intelligence: A Modern Approach' added to the library.
Book 'Clean Code' added to the library.
Book 'Agile Software Development, Principles, Patterns, and Practices' added to the library.
Book 'Refactoring: Improving the Design of Existing Code' added to the library.
Book 'Introduction to the Theory of Computation' added to the library.
Book 'Introduction to Algorithms' added to the library.
Book 'Design Patterns: Elements of Reusable Object-Oriented Software' added to the library.
Book 'Effective Java' added to the library.
Book 'The Mythical Man-Month: Essays on Software Engineering' added to the library.
Book 'The Pragmatic Programmer' added to the library.
Book 'Designing Data-Intensive Applications' added to the library.
Book 'Python Data Science Handbook' added to the library.
Book 'Artificial Intelligence: Foundations of Computational Agents' added to the library.
Book 'Computer Networking: A Top-Down Approach' added to the library.
Book 'Deep Learning with Python' added to the library.
Book 'Deep Learning' added to the library.
Book 'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow' added to the library.
Book 'Python Machine Learning By Example' added to the library.
Book 'Machine Learning: A Probabilistic Perspective' added to the library.
Book 'Fluent Python' added to the library.
Book with ISBN 978-0134093413 already exists in the library.

All books in the library:
[{'title': 'Operating System Concepts', 'author': 'Abraham Silberschatz', 'publisher': 'Wiley', 'volume': 10, 'year': 2020}, {'title': 'Modern Operating Systems', 'author': 'Andrew S. Tanenbaum', 'publisher': 'Pearson', 'volume': 4, 'year': 2020}, {'title': 'Structure and Interpretation of Computer Programs', 'author': 'Harold Abelson', 'publisher': 'MIT Press', 'volume': 2, 'year': 2020}, {'title': 'Data Structures and Algorithm Analysis in C++', 'author': 'Mark Allen Weiss', 'publisher': 'Pearson', 'volume': 4, 'year': 2021}, {'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell', 'publisher': 'Pearson', 'volume': 4, 'year': 2021}, {'title': 'Clean Code', 'author': 'Robert C. Martin', 'publisher': 'Pearson', 'volume': 1, 'year': 2021}, {'title': 'Agile Software Development, Principles, Patterns, and Practices', 'author': 'Robert C. Martin', 'publisher': 'Pearson', 'volume': 1, 'year': 2020}, {'title': 'Refactoring: Improving the Design of Existing Code', 'author': 'Martin Fowler', 'publisher': 'Pearson', 'volume': 2, 'year': 2020}, {'title': 'Introduction to the Theory of Computation', 'author': 'Michael Sipser', 'publisher': 'Cengage Learning', 'volume': 3, 'year': 2021}, {'title': 'Introduction to Algorithms', 'author': 'Thomas H. Cormen', 'publisher': 'MIT Press', 'volume': 3, 'year': 2022}, {'title': 'Design Patterns: Elements of Reusable Object-Oriented Software', 'author': 'Erich Gamma', 'publisher': 'Pearson', 'volume': 1, 'year': 2021}, {'title': 'Effective Java', 'author': 'Joshua Bloch', 'publisher': 'Pearson', 'volume': 3, 'year': 2021}, {'title': 'The Mythical Man-Month: Essays on Software Engineering', 'author': 'Frederick P. Brooks Jr.', 'publisher': 'Addison-Wesley', 'volume': 2, 'year': 2020}, {'title': 'The Pragmatic Programmer', 'author': 'Andrew Hunt', 'publisher': 'Addison-Wesley', 'volume': 2, 'year': 2021}, {'title': 'Designing Data-Intensive Applications', 'author': 'Martin Kleppmann', 'publisher': "O'Reilly Media", 'volume': 1, 'year': 2021}, {'title': 'Python Data Science Handbook', 'author': 'Jake VanderPlas', 'publisher': "O'Reilly Media", 'volume': 1, 'year': 2020}, {'title': 'Artificial Intelligence: Foundations of Computational Agents', 'author': 'David L. Poole', 'publisher': 'Cambridge University Press', 'volume': 2, 'year': 2020}, {'title': 'Computer Networking: A Top-Down Approach', 'author': 'James F. Kurose', 'publisher': 'Pearson', 'volume': 6, 'year': 2020}, {'title': 'Deep Learning with Python', 'author': 'Francois Chollet', 'publisher': 'Manning Publications', 'volume': 1, 'year': 2020}, {'title': 'Deep Learning', 'author': 'Ian Goodfellow', 'publisher': 'MIT Press', 'volume': 1, 'year': 2020}, {'title': 'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow', 'author': 'Aurélien Géron', 'publisher': "O'Reilly Media", 'volume': 2, 'year': 2020}, {'title': 'Python Machine Learning By Example', 'author': 'Yuxi (Hayden) Liu', 'publisher': 'Apress', 'volume': 2, 'year': 2020}, {'title': 'Machine Learning: A Probabilistic Perspective', 'author': 'Kevin P. Murphy', 'publisher': 'MIT Press', 'volume': 1, 'year': 2022}, {'title': 'Fluent Python', 'author': 'Luciano Ramalho', 'publisher': "O'Reilly Media", 'volume': 2, 'year': 2020}]

Retrieving book with ISBN 978-0134670959:
{'title': 'Operating System Concepts', 'author': 'Abraham Silberschatz', 'publisher': 'Wiley', 'volume': 10, 'year': 2020}

Removing book with ISBN 978-0134670959:
Book with ISBN 978-0134670959 removed from the library.

Checking availability of book with ISBN 978-0134670959:
False

Searching for books with title 'Data Structures':
[{'title': 'Data Structures and Algorithm Analysis in C++', 'author': 'Mark Allen Weiss', 'publisher': 'Pearson', 'volume': 4, 'year': 2021}]       

Updating book with ISBN 978-0133591629:
Book with ISBN 978-0133591629 updated.
{'title': 'Modern Operating Systems', 'author': 'Andrew Tanenbaum', 'publisher': 'Pearson', 'volume': 4, 'year': 2020}

All books in the library after updates:
[{'title': 'Modern Operating Systems', 'author': 'Andrew Tanenbaum', 'publisher': 'Pearson', 'volume': 4, 'year': 2020}, {'title': 'Structure and Interpretation of Computer Programs', 'author': 'Harold Abelson', 'publisher': 'MIT Press', 'volume': 2, 'year': 2020}, {'title': 'Data Structures and Algorithm Analysis in C++', 'author': 'Mark Allen Weiss', 'publisher': 'Pearson', 'volume': 4, 'year': 2021}, {'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell', 'publisher': 'Pearson', 'volume': 4, 'year': 2021}, {'title': 'Clean Code', 'author': 'Robert C. Martin', 'publisher': 'Pearson', 'volume': 1, 'year': 2021}, {'title': 'Agile Software Development, Principles, Patterns, and Practices', 'author': 'Robert C. Martin', 'publisher': 'Pearson', 'volume': 1, 'year': 2020}, {'title': 'Refactoring: Improving the Design of Existing Code', 'author': 'Martin Fowler', 'publisher': 'Pearson', 'volume': 2, 'year': 2020}, {'title': 'Introduction to the Theory of Computation', 'author': 'Michael Sipser', 'publisher': 'Cengage Learning', 'volume': 3, 'year': 2021}, {'title': 'Introduction to Algorithms', 'author': 'Thomas H. Cormen', 'publisher': 'MIT Press', 'volume': 3, 'year': 2022}, {'title': 'Design Patterns: Elements of Reusable Object-Oriented Software', 'author': 'Erich Gamma', 'publisher': 'Pearson', 'volume': 1, 'year': 2021}, {'title': 'Effective Java', 'author': 'Joshua Bloch', 'publisher': 'Pearson', 'volume': 3, 'year': 2021}, {'title': 'The Mythical Man-Month: Essays on Software Engineering', 'author': 'Frederick P. Brooks Jr.', 'publisher': 'Addison-Wesley', 'volume': 2, 'year': 2020}, {'title': 'The Pragmatic Programmer', 'author': 'Andrew Hunt', 'publisher': 'Addison-Wesley', 'volume': 2, 'year': 2021}, {'title': 'Designing Data-Intensive Applications', 'author': 'Martin Kleppmann', 'publisher': "O'Reilly Media", 'volume': 1, 'year': 2021}, {'title': 'Python Data Science Handbook', 'author': 'Jake VanderPlas', 'publisher': "O'Reilly Media", 'volume': 1, 'year': 2020}, {'title': 'Artificial Intelligence: Foundations of Computational Agents', 'author': 'David L. Poole', 'publisher': 'Cambridge University Press', 'volume': 2, 'year': 2020}, {'title': 'Computer Networking: A Top-Down Approach', 'author': 'James F. Kurose', 'publisher': 'Pearson', 'volume': 6, 'year': 2020}, {'title': 'Deep Learning with Python', 'author': 'Francois Chollet', 'publisher': 'Manning Publications', 'volume': 1, 'year': 2020}, {'title': 'Deep Learning', 'author': 'Ian Goodfellow', 'publisher': 'MIT Press', 'volume': 1, 'year': 2020}, {'title': 'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow', 'author': 'Aurélien Géron', 'publisher': "O'Reilly Media", 'volume': 2, 'year': 2020}, {'title': 'Python Machine Learning By Example', 'author': 'Yuxi (Hayden) Liu', 'publisher': 'Apress', 'volume': 2, 'year': 2020}, {'title': 'Machine Learning: A Probabilistic Perspective', 'author': 'Kevin P. Murphy', 'publisher': 'MIT Press', 'volume': 1, 'year': 2022}, {'title': 'Fluent Python', 'author': 'Luciano Ramalho', 'publisher': "O'Reilly Media", 'volume': 2, 'year': 2020}]
'''