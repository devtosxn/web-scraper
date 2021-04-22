import unittest
from plotter import Plotter


class TestPlotter(unittest.TestCase):

    def setUp(self):
        sorted_list = [('Smile', 65), ('Game', 60), ('Class', 55), ('Orange', 50), ('Study', 45), ('News', 35),
                       ('Smart', 19)]
        self.plotter = Plotter(sorted_list)

    def test_extract_words(self):
        self.assertEqual(self.plotter.extract_words(), ['Smile', 'Game', 'Class', 'Orange', 'Study', 'News', 'Smart'])

    def test_extract_words_frequency(self):
        self.assertEqual(self.plotter.extract_words_frequency(), [65, 60, 55, 50, 45, 35, 19])

    def test_plot_bar_chart(self):
        self.data = self.plotter
        self.assertIsNone(self.plotter.plot_bar_chart(), None)

    def test_plot_pie_chart(self):
        self.assertIsNone(self.plotter.plot_pie_chart(), None)

    def tearDown(self):
        self.plotter = None


if __name__ == '__main__':
    unittest.main()
