#!/usr/bin/env python3
""" filtered_logger module
"""
import re


def filter_datum(fields, redaction, message, separator):
    """ TEST """
    for field in fields:
        pattern = fr'{field}=.*?(?={separator})'
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message
