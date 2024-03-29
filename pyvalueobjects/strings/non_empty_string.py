from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.strings.string import String


class NonEmptyString(String):

    def __init__(self, value: str):
        super().__init__(value)

    def _validate(self, value):
        super()._validate(value)
        if value == '':
            raise ValueObjectError('Value must be a non empty strings.')
