import unittest

class TestAdd(unittest.TestCase):
    def test_Positive(self):
        self.assertEqual(1+1, 2)

if __name__ == '__main__':
    unittest.main()
