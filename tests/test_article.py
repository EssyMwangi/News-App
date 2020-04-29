import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    """
    ArticleTest class to test the behaviour of the Source class
    """

    def setUp(self):
        self.new_article = Articles("Vox.com", "Riley", "Hurricane Dorian", "The storm has left at least 43 dead",
                                    "http//www.vox.com", "https://www.thehindu.com/static/theme/default/base/img/og-image.jpg", "2019-09-07T19:41:51Z")

    def instance_test(self):
        self.assertTrue(isinstance(self.new_article, Articles))


    def test_check_instance_variables(self):
        self.assertEqual(self.new_article.source, 'Vox.com')
        self.assertEquals(self.new_article.author, 'Riley')
        self.assertEquals(self.new_article.title, 'Hurricane Dorian')
        self.assertEquals(self.new_article.description, 'The storm has left at least 43 dead')
        self.assertEquals(self.new_article.url, 'http//www.vox.com')
        self.assertEquals(self.new_article.urlToImage,'https://www.thehindu.com/static/theme/default/base/img/og-image.jpg')
        self.assertEquals(self.new_article.publishedAt, '2019-09-07T19:41:51Z')