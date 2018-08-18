import unittest
from pott.ngram import Ngram


class TestNgram(unittest.TestCase):

    def test_take_in(self):
        ngram = Ngram()
        text = 'This is a sentence for this class.'
        ngram.take_in(text)
        self.assertEqual(ngram.n_to_ngram[1]['this'], 1)
        self.assertEqual(ngram.n_to_ngram[1]['is'], 1)
        self.assertEqual(ngram.n_to_ngram[1]['class.'], 1)
        self.assertEqual(ngram.n_to_ngram[2]['This is'], 1)


if __name__ == "__main__":
    unittest.main()
