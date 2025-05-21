#!/usr/bin/env python3
"""
This module provides utilities for handling
and protecting sensitive data in logs and databases.
"""
import re
import logging

from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to redact.

        Args:
            fields (List[str]): fields to be obfuscated in logs.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, obfuscating sensitive data.

        Args:
            record (logging.LogRecord): log record to format.

        Returns:
            str: formatted log message with sensitive fields redacted.
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


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
