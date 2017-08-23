#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from mseye.skeleton import fib

__author__ = "Paulo Matos"
__copyright__ = "Paulo Matos"
__license__ = "proprietary"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
