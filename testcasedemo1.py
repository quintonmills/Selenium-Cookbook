import unittest

class TestCaseDemo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("#"*30)
        print("I will run once before all tests")
        print("#"*30)
    def setUp(self):
        print("test set up method")
    def test_methodA(self):
        print("yeah boi method A")
    def test_methodB(self):
        print("boi method B")
    def tearDOwn(self):
        print("Test tear down method")
    @classmethod
    def tearDownClass(cls):
        print("#"*30)
        print("I will run once before all tests")
        print("#"*30)

if __name__ == '__main__':
    unittest.main(verbosity=2)