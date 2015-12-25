__author__ = 'du'

import datetime
from json import JSONEncoder


class DatetimeJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        return JSONEncoder.default(self, obj)
