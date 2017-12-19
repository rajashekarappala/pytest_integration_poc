# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from sampleapp.views import add_numbers
# Create your tests here.
class TestingViews(TestCase):
    def setUp(self):
        pass

    def test_both_strings(self):
        self.assertEqual(add_numbers("string",4) , "Both arguments are not numbers")

    def test_first_is_string(self):
        self.assertEqual(add_numbers("string",4) , "first argument is not a number")

    def test_second_is_string(self):
        self.assertEqual(add_numbers(3,"string") , "second argument is not a number")

    def test_if_adds(self):
        self.assertEqual(add_numbers(4,5.6), 9.6)