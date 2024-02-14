import argparse
import unittest

parser = argparse.ArgumentParser(description='Calculate values of two numbers')
parser.add_argument('-excu',default="Local", type=str, help='string1')
parser.add_argument('-browser',default='chrome' ,type=str, help='string2')
args = parser.parse_args()
excu=args.excu
browser=args.browser
if __name__ == '__main__':
    from Tests.maintest1 import TestCart
    testLoad = unittest.TestLoader()
    testSuite = testLoad.loadTestsFromTestCase(TestCart)
    runner = unittest.TextTestRunner()
    runner.run(testSuite)