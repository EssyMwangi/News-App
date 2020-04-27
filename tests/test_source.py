import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    """
    SourceTest class to test the behaviour of the Source class
    """

    def setUp(self):
        """
        Method that runs before each other test runs
        """
        self.new_source = Source('abc-news', 'ABC news', 'Your trusted source for breaking news',
                                 "https://abcnews.go.com", "general", "en", "us")

    def instance_test(self):
        self.assertTrue(isinstance(self.new_source, Source))
