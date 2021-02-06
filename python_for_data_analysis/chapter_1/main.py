import json

path = 'usagov_bitly_data2012-03-16-1331923249'
print(open(path).readline())

records = [json.loads(line) for line in open(path, 'rb')]
print(records[0])
