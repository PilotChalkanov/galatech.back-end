from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxFileSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        file_size = value.file.size
        if file_size > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError("Max file size is 5.00 MB")

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * (1024**2)
