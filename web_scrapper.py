from bs4 import BeautifulSoup
import re
from collections import Counter
from src.utils import common_words
import requests


class WebScraper:
    """
    A Class to scrape data from user provided url

    Attribute
    ----------
    url : str
        uniform resource locator provided by user

    Methods
    -------
    get_web_content()
        returns all the text scrapped from website in a string
    get_web_text()
        returns a list of only words matched within the original text scrapped
    filter_text()
        returns a list of relevant words
    get_word_count()
        returns a counter collection of the relevant words
    get_top_words()
        filters counter collection of relevant words and returns top 7
    print_common_word()
        prints the most common word in site to the user
    """
    def __init__(self, url):
        self.url = url

    def get_web_content(self):
        source = requests.get(self.url).text
        soup = BeautifulSoup(source, "html.parser")
        return soup.get_text()

    def get_web_text(self):
        text = self.get_web_content()
        match = re.findall(r"[a-zA-Z]+", text, re.IGNORECASE)
        return match

    def filter_text(self):
        raw_text_list = self.get_web_text()
        filtered_list = [item for item in raw_text_list if item not in common_words and len(item) >= 3]
        return filtered_list

    def get_words_count(self):
        filtered_list = self.filter_text()
        return Counter(filtered_list)

    def get_top_words(self):
        full_list = self.get_words_count()
        return full_list.most_common(7)

    def print_common_word(self):
        top_words = self.get_top_words()
        return f'The most common word on {self.url} is {top_words[0][0]}'


