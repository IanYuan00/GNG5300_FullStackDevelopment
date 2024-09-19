import re

def validate_phone(phone):
    pattern = r'\(\d{3}\)\d{3}-\d{4}'
    return bool(re.fullmatch(pattern, phone))

def validate_email(email):
    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    return bool(re.fullmatch(pattern, email))

def get_validated_input(prompt, validation_func, error_msg):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print(error_msg)
