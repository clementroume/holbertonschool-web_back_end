#!/usr/bin/env python3
"""
This module provides utilities for handling
and protecting sensitive data in logs and databases.
"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
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
