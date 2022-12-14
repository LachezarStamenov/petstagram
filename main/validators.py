from django.core.validators import ValidationError


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(self.max_size))