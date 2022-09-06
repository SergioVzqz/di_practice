from datetime import datetime
from typing import Dict
from dateutil.relativedelta import relativedelta

from ivalidator import Validator

VALID_AGE = 18
TODAY = datetime.today()
LIMIT_DAY = datetime.strptime(f'26/06/{TODAY.year}',"%d/%m/%Y")

class AgeValidator(Validator):
    def __init__(self, birthdate: datetime):
        self._validate_format(birthdate)
        self.birthdate = self.validate_value(datetime.strptime(birthdate,"%d/%m/%Y"))

    def validate_value(self, birthdate):
        result: Dict = {
            'approved': False,
            'reason': ''
        }
        age_to_today = relativedelta(TODAY.date(), birthdate.date()).years
        age_at_limit_day = relativedelta(LIMIT_DAY.date(), birthdate.date()).years

        if age_to_today <= 0 or age_at_limit_day <= 0:
            raise ValueError("The birthdate is invalid, need to be before today or before the limit day.")

        if age_at_limit_day >= VALID_AGE:
            result = {
                'approved': True,
                'reason': "You have the valid age."
            }

        if age_at_limit_day <= VALID_AGE:
            result = {
                'approved': False,
                'reason': "You don't have the valid age."
            }

        return result

    def _validate_format(self, date) -> None:
        try:
            datetime.strptime(date,"%d/%m/%Y")
        except ValueError:
            raise ValueError(f"The date {date} has an incorrect format, expected: DD/MM/YYYY.")