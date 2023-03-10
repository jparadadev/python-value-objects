import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.numbers.nullable_int import NullableInt


class TestNullableIntValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = NullableInt(39)
        self.assertEqual(39, vo.value())

    def test_from_string_method_returns_int(self):
        vo = NullableInt.from_str('39')
        self.assertEqual(39, vo.value())

    def test_from_float_method_returns_int(self):
        vo = NullableInt.from_float(39.0)
        self.assertEqual(39, vo.value())

    def test_zero_value_return_input_value(self):
        vo = NullableInt(0)
        self.assertEqual(0, vo.value())

    def test_zero_from_string_method_returns_int(self):
        vo = NullableInt.from_str('0')
        self.assertEqual(0, vo.value())

    def test_zero_from_float_method_returns_int(self):
        vo = NullableInt.from_float(0.0)
        self.assertEqual(0, vo.value())

    def test_negative_value_return_input_value(self):
        vo = NullableInt(-39)
        self.assertEqual(-39, vo.value())

    def test_from_string_method_returns_negative_int(self):
        vo = NullableInt.from_str('-39')
        self.assertEqual(-39, vo.value())

    def test_from_float_method_returns_negative_int(self):
        vo = NullableInt.from_float(-39.0)
        self.assertEqual(-39, vo.value())

    def test_from_string_with_not_numerical_format_raise_error(self):
        self.assertRaises(ValueObjectError, NullableInt.from_str, 'patata')

    def test_from_float_with_decimals_raise_error(self):
        self.assertRaises(ValueObjectError, NullableInt.from_float, 39.1)

    def test_from_str_number_with_no_decimals(self):
        vo = NullableInt.from_str('39.0')
        self.assertEqual(39, vo.value())

    def test_from_str_negative_number_with_no_decimals(self):
        vo = NullableInt.from_str('-39.0')
        self.assertEqual(-39, vo.value())

    def test_from_str_number_with_decimals_raises_error(self):
        self.assertRaises(ValueObjectError, NullableInt.from_float, '39.1')

    def test_from_str_negative_number_with_decimals_raises_error(self):
        self.assertRaises(ValueObjectError, NullableInt.from_float, '-39.1')

    def test_none_value_return_none(self):
        vo = NullableInt(None)
        self.assertEqual(None, vo.value())
