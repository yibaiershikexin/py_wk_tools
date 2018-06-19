# -*- coding: utf-8 -*-
from nose.tools import assert_equal
import unittest

'''
nosetests -s test_sample.py

'''

def setUp():
    print("============test math module setup==============")


def teardown():
    print("============test math module teardown==============")


def test_math_add():
    result = 4 + 5
    print("================test_math_add============")
    assert_equal(10, result)


class test_math3():
    def setUp(self):
        print("============test math class setup==============")

    def teardown(self):
        print("============test math class teardown==============")

    def test_math_square(self):
        print("=============== test_math_square================ ")
        assert_equal(9, 3 ** 2)

    def test_math_sub(self):
        print("=============== test_math_sub================ ")
        assert_equal(1, 3 - 2)


class test_math2(unittest.TestCase):

    def test_math_multipy(self):
        print("=============== test_math_multipy================ ")
        assert_equal(8, 2 * 4)
