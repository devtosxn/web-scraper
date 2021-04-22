from plotter import Plotter
import requests
from web_scrapper import WebScraper
import time


def url_is_valid(url):
    """ takes in url as parameter and returns True if a connection can be established else returns None """
    try:
        result = requests.get(url)
        result.raise_for_status()
    except requests.exceptions.ConnectionError:
        print('Connection error! Check that your internet works')
    except requests.exceptions.HTTPError:
        print('HTTP error')
    except requests.exceptions.RequestException:
        print("Connection was not established. Check URL")
    else:
        return True


def get_url():
    """ prompts user to enter a website to scrape"""
    original_url = input('Enter the website you want to scrape: ')
    return original_url


def attempt_website_scrape():
    """ scrapes and analyses text from website if a connection is established with website provided by user"""
    url = get_url()
    flag = url_is_valid(url)
    if flag:
        web_scraper = WebScraper(url)
        print(web_scraper.print_common_word())
        plot_list = web_scraper.get_top_words()
        plotter = Plotter(plot_list)
        time.sleep(0.5)
        plotter.plot_bar_chart()
        plotter.plot_pie_chart()
