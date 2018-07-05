import datetime
import json
import decimal


json_1 = {'num': 1112, 'date': datetime.datetime.now()}
data = {'key1': 'string', 'key2': 10, 'key3': decimal.Decimal('1.45')}


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.__str__()
        return json.JSONEncoder.default(self, obj)


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)


class ExtendJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)

        if isinstance(obj, datetime.datetime):
            return obj.__str__()

        return super(ExtendJSONEncoder, self).default(obj)


print(json.dumps(json_1, cls=ExtendJSONEncoder))
print(json.dumps(data, cls=ExtendJSONEncoder))
