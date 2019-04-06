import unittest
import bianlaTest

suit = unittest.TestSuite
suit.addTest(bianlaTest("test_case_01"))

unittest.TextTestRunner.run(suit)