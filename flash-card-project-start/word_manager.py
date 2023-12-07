import pandas
import random


class WordManager:
    def __init__(self):
        try:
            self.words = pandas.read_csv('words_to_learn.csv')
        except FileNotFoundError:
            self.words = pandas.read_csv('data/french_words.csv')
        finally:
            self.words = self.words.to_dict(orient='records')
            self.chosen_pair = None

    def choose_word(self):
        try:
            self.chosen_pair = random.choice(self.words)
        except IndexError:
            self.words = pandas.read_csv('data/french_words.csv')
            self.words = self.words.to_dict(orient='records')
            self.chosen_pair = None
        finally:
            self.chosen_pair = random.choice(self.words)
        french_wd = self.chosen_pair['French']
        return french_wd

    def english_word(self):
        eng_wd = self.chosen_pair["English"]
        return eng_wd

    def remove_pair(self):
        self.words.remove(self.chosen_pair)
        words_to_learn = pandas.DataFrame(self.words)
        words_to_learn.to_csv('words_to_learn.csv')
