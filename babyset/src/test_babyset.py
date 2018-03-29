# test_babyset.py
import unittest

from baby_set import BabySet

class TestBabySetMethods(unittest.TestCase):

    def test_init(self):
        bset = BabySet([2, 4, 4])
        self.assertEqual(bset.size(), 2)

    def test_init_empty(self):
        pass

    def test_add(self):
        bset = BabySet([2, 4, 4])
        bset.add(4)
        self.assertEqual(bset.size(), 2)
    
    def test_addSeq(self):
        bset = BabySet([2, 4, 4])
        bset.addSeq([3, 4, 5,])
        self.assertEqual(bset.size(), 4)

    def test_get(self):
    	bset = BabySet([2, 4, 4])
        with self.assertRaises(KeyError):
            bset.get(3)

    def test_remove(self):
        pass

    def test_clear(self):
        pass

if __name__ == '__main__':
    unittest.main()