# Create by Fedor Tsyganov on July 13th 2017

import unittest
import sys

from range import *


class RangeTestCase(unittest.TestCase):

    ERROR_MSG_ARBITRARY = 'Arbitrary Range is invalid'
    ERROR_MSG_ZIPCODE = 'Zip Code Range is invalid'

    def setUp(self):
        self.expected_result_arbitrary = RangeUtil()
        self.expected_result_arbitrary.add_range(Range(2, 5))
        self.expected_result_arbitrary.add_range(Range(20, 35))

        self.expected_result_zipcode_1 = RangeUtil()
        self.expected_result_zipcode_1.add_range(Range(94133, 94133))
        self.expected_result_zipcode_1.add_range(Range(94200, 94299))
        self.expected_result_zipcode_1.add_range(Range(94600, 94699))

        self.expected_result_zipcode_2 = RangeUtil()
        self.expected_result_zipcode_2.add_range(Range(94133, 94133))
        self.expected_result_zipcode_2.add_range(Range(94200, 94399))


    def test_arbitrary_range(self):
        print >> sys.stdout, '>> Test Arbitatry Range'
        actual_result = RangeUtil()
        actual_result.add_range(Range(3, 3))
        actual_result.add_range(Range(4, 5))
        actual_result.add_range(Range(2, 4))
        actual_result.add_range(Range(22, 34))
        actual_result.add_range(Range(20, 28))
        actual_result.add_range(Range(3, 4))
        actual_result.add_range(Range(34, 35))
        self.assertEqual(self.expected_result_arbitrary.__str__(), actual_result.__str__(), msg=self.ERROR_MSG_ARBITRARY)

    def test_zipcode_range_1(self):
        print >> sys.stdout, '>> Test Zip Code Range. Data 1'
        actual_result = RangeUtil()
        actual_result.add_range(Range(94133, 94133))
        actual_result.add_range(Range(94200, 94299))
        actual_result.add_range(Range(94600, 94699))
        self.assertEqual(self.expected_result_zipcode_1.__str__(), actual_result.__str__(), msg=self.ERROR_MSG_ZIPCODE)

    def test_zipcode_range_2(self):
        print >> sys.stdout, '>> Test Zip Code Range. Data 2'
        actual_result = RangeUtil()
        actual_result.add_range(Range(94133, 94133))
        actual_result.add_range(Range(94200, 94299))
        actual_result.add_range(Range(94226, 94399))
        self.assertEqual(self.expected_result_zipcode_2.__str__(), actual_result.__str__(), msg=self.ERROR_MSG_ZIPCODE)