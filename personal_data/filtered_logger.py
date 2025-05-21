#!/usr/bin/env python3
""" filtered_logger module
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Replace the values of specified fields in the message with
    the redaction string.

    Args:
        fields: List of field names to obfuscate.
        redaction: The string to replace the field values with.
        message: The original log message.
        separator: The separator between fields (e.g., ';').

    Returns:
        str: The log message with sensitive fields obfuscated.
    """
    for field in fields:
        pattern = fr'{field}=.*?(?={separator})'
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message
