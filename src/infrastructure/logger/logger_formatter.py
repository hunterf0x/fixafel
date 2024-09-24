"""This module defines a custom JSON formatter for logging."""

import json
from pythonjsonlogger import jsonlogger

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """Custom JSON formatter for logging."""

    def remove_field(self, log_record):
        """Removes specific fields from the log record.

        Args:
            log_record (dict): The log record dictionary.

        Returns:
            dict: The modified log record dictionary.
        """
        if 'taskName' in log_record:
            del log_record['taskName']
        return log_record

    def format(self, record):
        """Formats the log record as a JSON string.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The JSON-formatted log record.
        """
        log_record = super().format(record)
        log_record = json.loads(log_record)
        self.remove_field(log_record)
        return json.dumps(log_record)
