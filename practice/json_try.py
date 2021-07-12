#!/usr/local/bin/python3

import json

data ={
    'name'   : 'ACME',
    'shares' : 100,
    'price'  : 542.23
}

json_str = json.dumps(data)

print(json_str)

print(data)

data_cp = json.loads(json_str)
print(data_cp)


# If you want to handle the file rather than characters.
# json.dump(), json.load() should be used.


# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f);

# Reading data back
with open('data.json', 'r') as f:
    data2 = json.load(f)
    print(data2)


