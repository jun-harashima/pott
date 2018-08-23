import os
import pickle
import unittest
from unittest.mock import patch
from pott.ngram import Ngram

TEST_FILE = 'test.pickle'


class TestNgram(unittest.TestCase):

    def setUp(self):
        with open(TEST_FILE, mode='wb') as file:
            n_to_ngram = {}
            for n in range(1, 5):
                n_to_ngram[n] = {}
            pickle.dump(n_to_ngram, file)

    def tearDown(self):
        os.remove(TEST_FILE)

    @patch('pott.ngram.Ngram.NGRAM_FILE', TEST_FILE)
    def test_load(self):
        ngram = Ngram(5)
        text = 'This is a sentence for this class.'
        ngram.load(text)
        self.assertEqual(ngram.n_to_ngram[1]['this'], 1)
        self.assertEqual(ngram.n_to_ngram[1]['is'], 1)
        self.assertEqual(ngram.n_to_ngram[1]['class.'], 1)
        self.assertEqual(ngram.n_to_ngram[2]['This is'], 1)


if __name__ == "__main__":
    unittest.main()
