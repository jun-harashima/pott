import os
import pickle
from nltk.util import ngrams


class Ngram:

    DOT_DIR = os.environ['HOME'] + '/.pott'
    TXT_DIR = os.environ['HOME'] + '/.pott/txt'
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

    def reload(self, paper_by_id):
        os.remove(self.NGRAM_FILE)
        self.__init__()
        for paper in paper_by_id.values():
            print('counting N-gram in "' + paper.title + '"')
            with open(self.TXT_DIR + '/' + paper.id + '.txt', 'r') as txt_file:
                self.load(txt_file.read())

    def load(self, text):
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
