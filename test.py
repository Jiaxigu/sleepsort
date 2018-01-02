#-*- encoding: UTF-8 -*-
import unittest

from sleepsort import *

class SleepsortTestCases(unittest.TestCase):
        
    def test_negative_number(self):
        sample_negative_array = [-2, 3, 1, 6]
        with self.assertRaises(ValueError):
            sleepsort(sample_negative_array)
        
    def test_sorted(self):
        sample_short_array = [4, 2, 3, 1]
        self.assertEqual(sleepsort(sample_short_array), sorted(sample_short_array))
        
def suite_loader():
    test_cases = (SleepsortTestCases,)
    suite = unittest.TestSuite()
    for test_case in test_cases:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite_loader')
    