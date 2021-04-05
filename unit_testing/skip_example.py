import unittest


class MyTestCase(unittest.TestCase):


    @unittest.skip("Demostrating Skipping")
    def test_nothing(self):
        self.fail("Shouldn't happen")

    # @unittest.skipIf(mylib.__version__ < (1, 3),
    #                 "not supported in this library version")
    # def test_format(self):
    #     #Tests that work for only a certain version of the library
    #     pass

    # def test_windows_support(self):
    #     #windows specific testing code
    #     pass

    # def test_maybe_skipped(self):
    #     if not external_resource_available():
    #         self.skipTest('external resource not available')
    #     pass    
