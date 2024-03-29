import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.numbers.nullable_positive_or_zero_int import NullablePositiveOrZeroInt


class TestNullablePositiveIntValueObject(unittest.TestCase):

    def __init__(self, *args):
        super().__init__(*args)
        self._cls = NullablePositiveOrZeroInt

    def test_vo_equal_hash(self):
        original_vo_hash = hash(self._cls(39))
        equal_vo_hash = hash(self._cls(39))
        self.assertEqual(original_vo_hash, equal_vo_hash)

    def test_vo_different_hash(self):
        original_vo_hash = hash(self._cls(39))
        not_equal_vo_hash = hash(self._cls(93))
        self.assertNotEqual(original_vo_hash, not_equal_vo_hash)

    def test_vo_equality(self):
        original_vo = self._cls(39)
        equal_vo = self._cls(39)
        self.assertEqual(original_vo, equal_vo)

    def test_vo_different_equality(self):
        original_vo = self._cls(39)
        different_vo = self._cls(97)
        self.assertNotEqual(original_vo, different_vo)

    def test_value_return_input_value(self):
        vo = NullablePositiveOrZeroInt(39)
        self.assertEqual(39, vo.value())

    def test_from_string_method_returns_int(self):
        vo = NullablePositiveOrZeroInt.from_str('39')
        self.assertEqual(39, vo.value())

    def test_from_float_method_returns_int(self):
        vo = NullablePositiveOrZeroInt.from_float(39.0)
        self.assertEqual(39, vo.value())

    def test_zero_value_return_input_value(self):
        vo = NullablePositiveOrZeroInt(0)
        self.assertEqual(0, vo.value())

    def test_zero_from_string_method_returns_int(self):
        vo = NullablePositiveOrZeroInt.from_str('0')
        self.assertEqual(0, vo.value())

    def test_zero_from_float_method_returns_int(self):
        vo = NullablePositiveOrZeroInt.from_float(0.0)
        self.assertEqual(0, vo.value())

    def test_negative_value_raises_error(self):
        self.assertRaises(ValueObjectError, NullablePositiveOrZeroInt, -39)

    def test_from_string_method_raises_error(self):
        self.assertRaises(ValueObjectError, NullablePositiveOrZeroInt.from_str, '-39')

    def test_from_float_method_returns_negative_int(self):
        self.assertRaises(ValueObjectError, NullablePositiveOrZeroInt.from_float, -39.0)

    def test_from_string_with_not_numerical_format_raise_error(self):
        self.assertRaises(ValueObjectError, NullablePositiveOrZeroInt.from_str, 'patata')

    def test_from_float_with_decimals_raise_error(self):
        self.assertRaises(ValueObjectError, NullablePositiveOrZeroInt.from_float, 39.1)

    def test_from_str_number_with_no_decimals(self):
        vo = NullablePositiveOrZeroInt.from_str('39.0')
        self.assertEqual(39, vo.value())

    def test_from_str_negative_number_with_no_decimals(self):
        self.assertRaises(ValueObjectError, NullablePositiveOrZeroInt.from_str, '-39.0')

    def test_from_str_number_with_decimals_raises_error(self):
        self.assertRaises(ValueObjectError, NullablePositiveOrZeroInt.from_float, '39.1')

    def test_from_str_negative_number_with_decimals_raises_error(self):
        self.assertRaises(ValueObjectError, NullablePositiveOrZeroInt.from_float, '-39.1')

    def test_none_value_return_none(self):
        vo = NullablePositiveOrZeroInt(None)
        self.assertEqual(None, vo.value())
