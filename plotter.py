from matplotlib import pyplot as plt


class Plotter:
    """
    A Class to handle plotting of bar and pie charts of data scraped from user-provided website

    Attribute
    ----------
    sorted_list : list
        a sorted list of tuples with each containing a word and its count

    Methods
    -------
    extract_words()
        returns a list of words in the sorted list
    extract_words_frequency()
        returns a list of word counts in the sorted list
    plot_bar_char()
        plots a bar chart of words and their word count using the matplotlib library
    plot_pie_char()
        plots a pie chart of words and their word count using the matplotlib library
    """

    def __init__(self, sorted_list):
        self.sorted_list = sorted_list

    def extract_words(self):
        return [item[0] for item in self.sorted_list]

    def extract_words_frequency(self):
        return [item[1] for item in self.sorted_list]

    def plot_bar_chart(self):
        x = self.extract_words()
        y = self.extract_words_frequency()
        plt.bar(x, y)
        plt.show()

    def plot_pie_chart(self):
        x = self.extract_words()
        y = self.extract_words_frequency()
        plt.pie(y, labels=x, autopct="%1.2f%%")
        plt.show()

