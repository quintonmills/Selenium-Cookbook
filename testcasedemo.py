import unittest
class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("test set up method")
    def test_methodA(self):
        print("yeah boi method A")
    def test_methodB(self):
        print("boi method B")
    def tearDOwn(self):
        print("Test tear down method")
if __name__ == '__main__':
    unittest.main(verbosity=2)