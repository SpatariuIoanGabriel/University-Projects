import unittest


def run_all():
    loader = unittest.TestLoader()
    suite = loader.discover("./tests", pattern="*_test.py")
    unittest.TextTestRunner().run(suite)
