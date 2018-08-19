import os
import pickle
from nltk.util import ngrams


class Ngram:

    NGRAM_FILE = os.environ['HOME'] + '/.pott/ngram.pickle'

    def __init__(self, max_n=5):
        self.n_to_ngram = {}
        for n in range(1, max_n):
            self.n_to_ngram[n] = {}

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
