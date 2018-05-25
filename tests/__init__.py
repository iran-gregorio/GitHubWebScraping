import unittest


def get_tests():
    return full_suite()

def full_suite():
    from .webscrapingtest import Test

    testsuite = unittest.TestLoader().loadTestsFromTestCase(Test)

    return unittest.TestSuite([testsuite])
