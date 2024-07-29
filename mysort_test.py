import unittest
import random
import mysort

class TestSort(unittest.TestCase):
    
    def test_sorted(self):
        l = [1,2,3,4,5]
        self.assertEqual(sorted(l.copy()), mysort.mysort(l.copy()))

    def test_reversed(self):
        l = [7,6,5,4,3,2,1]
        self.assertEqual(sorted(l.copy()), mysort.mysort(l.copy()))

    def test_duplicates(self):
        l = [7,6,5,4, 4, 4, 4, 4,3,2,1]
        self.assertEqual(sorted(l.copy()), mysort.mysort(l.copy()))

    def test_negatives(self):
        l = [1, 2, 3, -1, -2, -3]
        self.assertEqual(sorted(l.copy()), mysort.mysort(l.copy()))

    def test_random(self):
        l = [1,22,55,2,3,1,1,777,123,654,123,456,999,1000,-1, -100, -200]
        self.assertEqual(sorted(l.copy()), mysort.mysort(l.copy()))

    def test_empty(self):
        l = []
        self.assertEqual(sorted(l.copy()), mysort.mysort(l.copy()))

    def test_single(self):
        l = [0]
        self.assertEqual(sorted(l.copy()), mysort.mysort(l.copy()))

    def test_big(self):
        l = []
        for i in range(10000):
            l.append(random.randint(-10000, 10000))
        self.assertEqual(sorted(l.copy()), mysort.mysort(l.copy()))

if __name__ == '__main__':
    unittest.main()
