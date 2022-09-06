from typing import Dict

from ivalidator import Validator


VALID_GPA = 6.0

class GpaValidator(Validator):
    def __init__(self, gpa: float):
        self._validate_format(gpa)
        self.gpa = self.validate_value(float(gpa))

    def validate_value(self, gpa):
        result: Dict[bool, str] = {
            'aproved': False,
            'reason': 'reason'
        }

        if gpa <= 0:
            raise ValueError("The gpa is invalid, can't be less than 0")
        if gpa >= VALID_GPA:
            result = {
                'aproved': True,
                'reason': "You have the valid GPA."}
        if gpa <= VALID_GPA:
            result = {
                'aproved': False,
                'reason': "You don't have the valid GPA."}

        return result

    def _validate_format(self, value):
        try:
            float(value)
        except ValueError:
            raise ValueError(f"{value} is not a number, please correct.")