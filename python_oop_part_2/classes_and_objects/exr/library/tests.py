from python_oop_part_2.classes_and_objects.exr.library.library import Library
from python_oop_part_2.classes_and_objects.exr.library.user import User
from python_oop_part_2.classes_and_objects.exr.library.registration import Registration


user = User(12, 'Peter')
library = Library()
registration = Registration()
registration.add_user(user, library)
library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets','The Prisoner of Azkaban','The Goblet of Fire','The Order of the Phoenix', 'The Half-Blood Prince', 'The Deathly Hallows']})
library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user)
print(user)
