import re


def is_valid(data_with_numbers):
    phone_number_pattern = r'(?:(?:\+7)|8|7)?[\+\s-]?\(?\d{3}\)?[\+\s-]?\d{3}[\+\s-]?\d{2}[\+\s-]?\d{2}'
    phone_numbers = re.findall(phone_number_pattern, data_with_numbers)
    return phone_numbers
