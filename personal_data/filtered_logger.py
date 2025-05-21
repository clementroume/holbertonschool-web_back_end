#!/usr/bin/env python3
"""
This module provides utilities for handling
and protecting sensitive data in logs and databases.
"""
import re
import logging

from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")
"""
List of personally identifiable information (PII) field names to redact.

These field names correspond to keys expected in log messages, and their values
will be replaced by a redaction string when passed through a RedactingFormatter
"""


class RedactingFormatter(logging.Formatter):
    """
    Formatter for log records that redacts sensitive fields.

    This class extends the default `logging.Formatter` to automatically
    obfuscate sensitive information in log messages before they are output.
    It uses a custom `filter_datum` function to replace specified fields
    with a redaction string.

    Attributes:
        REDACTION (str): The string used to replace sensitive data.
        FORMAT (str): The log message format.
        SEPARATOR (str): Character used to separate fields in the log message.
        fields (List[str]): List of field names to redact from log messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize a RedactingFormatter instance.

        Args:
            fields (List[str]): A list of field names whose values
                                should be redacted from the log message.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the specified log record, redacting sensitive fields.

        This method modifies the log record message by replacing the values
        of specified fields with the redaction string before formatting.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted and redacted log message.
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


def get_logger() -> logging.Logger:
    """
    Create and configure a logger for user data with sensitive field redaction.

    This logger is intended to output log messages while ensuring that
    personally identifiable information (PII) is obfuscated using a
    RedactingFormatter. The logger outputs to the standard stream and is
    configured to not propagate messages to parent loggers.

    Returns:
        logging.Logger: A logger instance named "user_data" with INFO level
                        and a redacting formatter applied.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    return logger
