from enum import Enum
from functools import wraps


class RegexEnum(Enum):
    BRAND = (
        r'^[A-Z][a-zA-Z\d]{1,24}$',
        [
            'First letter uppercase min 2 max 25 characters',
            'If your brand_models is missing, contact the administrator'
        ]
    )
    MODEL = (
        r'^[A-Z][a-zA-Z\d]{1,24}$',
        'First letter uppercase min 2 max 25 characters'
    )
    PASSWORD = (
        r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=(?:.*[`~!@#$%^&*()\-_+=\\\|\'\"\;\:\/?.>,<\[\]\{\}]){2,'
        r'})[a-zA-Z\d`~!@#$%^&*()\-_+=\\\|\'\"\;\:\/?.>,<\[\]\{\}]{8,30}$',
        [
            'min 1 lowercase ch',
            'min 1 uppercase ch',
            'min 1 digit',
            'min 1 special character',
            'length 8-30'
        ]
    )
    NAME = (
        r'^[А-ЯЁІЇЄҐ][А-яёЁіІїЇєЄґҐ]{1,49}$',
        [
            'Only cyrillic',
            'First letter uppercase',
            'min 2 max 50 ch'
        ]
    )
    DESCRIPTION = (
        r'^((?!\bfuck(ing)?|shit(ting)?|asshole?|bitch(es)?|damn?|hell?\b).)*$',
        [
            'Obscene language is defined in description, Please revise it'
        ]
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg


def count_description_calls(func):
    attempts = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal attempts
        attempts += 1
        return func(*args, **kwargs)

    wrapper.description_calls = attempts
    return wrapper