import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    """
    ArticleTest class to test the behaviour of the Source class
    """
    def setUp(self):
        self.new_article = Articles("Vox.com","Riley","Hurricane Dorian","The storm has left at least 43 dead","http//www.vox.com","https://www.thehindu.com/static/theme/default/base/img/og-image.jpg","2019-09-07T19:41:51Z")

    def instance_test(self):
        self.assertTrue(isinstance(self.new_article,Articles))

