# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numbers
from django.shortcuts import render


# Create your views here.
def add_numbers(a, b):
    if not isinstance(a, numbers.Number) and not isinstance(b, numbers.Number):
        return "Both arguments are not numbers"
    elif not isinstance(a, numbers.Number):
        return "first argument is not a number"
    elif not isinstance(b, numbers.Number):
        return "second argument is not a number"
    else:
        return a+b

    