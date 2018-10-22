import unittest
class assertDemo(unittest.TestCase):
    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a,"a is not false")
        b = True
        self.assertTrue(b, "b is not true")
    def test_assertEqual(self):
        a = "Qmoney"
        b = "Qmoney"
        self.assertEqual(a,b)
    def test_assertle(self):
        one = 11
        two = 120
        self.assertGreater(two,one,"two is larger than one")
    def test_assertOne(self):
        first = "BOy you look gud"
        second = "BOy you look gud"
        self.assertMultiLineEqual(first,second, "the lines are not equal")
    def test_dict(self):
        kingOfTheHill = {'hank':'hill', 'bobby':'hill', 'peggy':'hill'}
        kingOfTheHillToo = {'hank':'hill', 'bobby':'hill', 'peggy':'hill'}
        self.assertDictEqual(kingOfTheHill,kingOfTheHillToo,'the strings arent a match')
if __name__ == '__main__':
    unittest.main(verbosity=1)




