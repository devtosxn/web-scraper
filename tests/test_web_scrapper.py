import unittest
import collections
from web_scrapper import WebScraper


class TestWebScraper(unittest.TestCase):

    def setUp(self):
        self.url = 'http://www.python.org'
        self.web_scrapper = WebScraper(self.url)

    def test_get_web_content(self):
        self.assertIsInstance(self.web_scrapper.get_web_content(), str)

    def test_get_web_text(self):
        self.assertIsInstance(self.web_scrapper.get_web_text(), list)

    def test_filter_text(self):
        self.assertIsInstance(self.web_scrapper.filter_text(), list)

    def test_get_words_count(self):
        self.assertIsInstance(self.web_scrapper.get_words_count(), collections.Counter)

    def test_get_top_words(self):
        self.assertIsInstance(self.web_scrapper.get_top_words(), list)

    def test_print_common_word(self):
        self.assertEqual(self.web_scrapper.print_common_word(), f'The most common word on {self.url} is Python')

    def tearDown(self):
        self.web_scrapper = None


if __name__ == '__main__':
    unittest.main()
