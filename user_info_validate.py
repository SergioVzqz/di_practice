from datetime import datetime
from age_validator import AgeValidator
from gpa_validator import GpaValidator
from graduation_date_validator import GraduationDateValidator

class UserInfoValidate():
    def __init__(self, birthdate: datetime, gpa: float, graduation_date: datetime):
        self.age_result = AgeValidator(birthdate)
        self.gpa_result = GpaValidator(gpa)
        self.graduation_date_result = GraduationDateValidator(graduation_date)