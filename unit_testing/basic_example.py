import unittest

class TestStringMethods(unittest.TestCase):
    
    @unittest.skip('Demostrating Skip')
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO',msg="correct")

    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        #Check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_upper'))
    suite.addTest(TestStringMethods('test_isupper'))
    return suite

if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())