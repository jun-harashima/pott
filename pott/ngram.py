import os
import pickle
from nltk.util import ngrams


class Ngram:

    DOT_DIR = os.environ['HOME'] + '/.pott'
    NGRAM_FILE = os.environ['HOME'] + '/.pott/ngram.pickle'

    def __init__(self, max_n=5):
        if not os.path.isdir(self.DOT_DIR):
            os.mkdir(self.DOT_DIR)

        if not os.path.isfile(self.NGRAM_FILE):
            self.n_to_ngram = {}
            for n in range(1, max_n):
                self.n_to_ngram[n] = {}
            self._save()

        with open(self.NGRAM_FILE, 'rb') as file:
            self.n_to_ngram = pickle.load(file)

    def take_in(self, text):
        for n in self.n_to_ngram.keys():
            for line in text.split('\n'):
                for ngram in ngrams(line.split(), n):
                    ngram = ' '.join(ngram)
                    if ngram not in self.n_to_ngram[n]:
                        self.n_to_ngram[n][ngram] = 1
                    else:
                        self.n_to_ngram[n][ngram] += 1
        self._save()

    def _save(self):
        with open(self.NGRAM_FILE, mode='wb') as file:
            pickle.dump(self.n_to_ngram, file)
