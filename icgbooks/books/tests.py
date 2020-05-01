from django.test import TestCase
from icgbooks.books.models import Book
# Create your tests here.


class BookTestCase(TestCase):
    def setUp(self) -> None:
        Book.objects.create(title="Test book", pages=612)

    def test_book_get(self):
        book = Book.objects.get(pages__exact=612)
        self.assertEqual(book.pages, 612)
