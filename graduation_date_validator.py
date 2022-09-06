from datetime import datetime
from typing import Dict

from ivalidator import Validator

TODAY = datetime.today()
LIMIT_DAY = datetime.strptime(f'26/06/{TODAY.year}',"%d/%m/%Y")

class GraduationDateValidator(Validator):

    def __init__(self, graduation_date: datetime):
        self._validate_format(graduation_date)
        self.graduation_date = graduation_date

    def validate_value(self, graduation_date) -> Dict:
        result: Dict = {
            'approved': False,
            'reason': ''
        }
        graduation_date_formatted = datetime.strptime(graduation_date, "%d/%m/%Y")

        if TODAY.date() > LIMIT_DAY.date():
            result = {
                'approved': False,
                'reason': 'The limit day has passed, please wait for the next year'
            }

        if graduation_date_formatted.date() > LIMIT_DAY.date():
            result = {
                'approved': False,
                'reason': 'The graduation day is later than the limit day to enter, please wait for the next year'
            }

        if graduation_date_formatted.date() <= LIMIT_DAY.date():
            result = {
                'approved': True,
                'reason': 'The graduation date if before the limit day, you can take the exam'
            }

        return result

    def _validate_format(self, date) -> None:
        try:
            datetime.strptime(date,"%d/%m/%Y")
        except ValueError:
            raise ValueError(f"The date {date} has an incorrect format, it should be DD/MM/YYYY")