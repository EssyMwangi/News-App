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

    def test_check_instance_variables(self):
        '''
        Test case to check if the objects are instansiated correctly
        '''
        self.assertEquals(self.new_source.id, 'abc-news')
        self.assertEquals(self.new_source.name, 'ABC news')
        self.assertEquals(self.new_source.description, 'Your trusted source for breaking news')
        self.assertEquals(self.new_source.url, "https://abcnews.go.com")
        self.assertEquals(self.new_source.category, 'general')
        self.assertEquals(self.new_source.language, 'en')
        self.assertEquals(self.new_source.country, 'us')