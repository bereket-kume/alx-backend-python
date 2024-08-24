#!/usr/bin/env python3
"""
Test fro access_nested_map function in utils
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Union
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    class to test  access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected: Union[Mapping, int]
    ) -> None:
        """
        Test the acces_nested_map funtion
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Exception
    ) -> None:
        """
        Use the assertRaises context manager to test
        that KeyError
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)