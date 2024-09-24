import json
from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def __init__(self, *args, **kwargs):
        super(CustomJsonFormatter, self).__init__(*args, **kwargs)

    def remove_field(self, log_record):
        if 'taskName' in log_record:
            del log_record['taskName']
        return log_record

    def format(self, record):
        log_record = super(CustomJsonFormatter, self).format(record)
        log_record = json.loads(log_record)
        self.remove_field(log_record)
        return json.dumps(log_record)
