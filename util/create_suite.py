import unittest
import os
path = os.path.abspath(os.path.dirname(__file__))


class CreateSuite:
    def creatsuite(self):
        suite = unittest.TestSuite()
        test_dir = path+"..//..//case//case//"
        discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py", top_level_dir=None)
        for test_suite in discover:
            for test_case in test_suite:
                suite.addTest(test_case)
        return suite
