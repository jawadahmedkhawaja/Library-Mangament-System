import random
from faker import Faker
from Books.models import Book, Category

def seed_db():
    book_categories = [
        "Fiction",
        "Fantasy",
        "Mystery/Thriller",
        "Romance",
        "Historical Fiction",
        "Self-Help",
        "Biography/Autobiography",
        "Educational/Academic"
    ]

    for category in book_categories:
        Category.objects.create(name=category)





    fake = Faker()

    # Generate 100 book entries
    books = []
    for _ in range(100):
        book = {
            "title": fake.sentence(nb_words=4).rstrip('.'),
            "author": fake.name(),
            "isbn": fake.isbn13(),
            "quantity": random.randint(5, 50),
        }
        book["available_count"] = random.randint(0, book["quantity"])
        category_name = random.choice(book_categories)
        category_instance = Category.objects.filter(name=category_name).first()

        Book.objects.create(
                category = category_instance,
                title = book['title'],
                author = book['author'],
                isbn = book['isbn'],
                quantity = book['quantity'],
                available_count = book['available_count'],
        )




