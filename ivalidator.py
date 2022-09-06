from abc import ABC, abstractmethod

class Validator(ABC):

    @abstractmethod
    def validate_value():
        return NotImplementedError

    @abstractmethod
    def _validate_format():
        return NotImplementedError