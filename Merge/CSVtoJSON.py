""" import json

input_dict = {'foo': 3, 'bar': 1}
result = []

for k, v in input_dict.items():
    result.append({'key': k, 'value': v})

print(json.dumps(result)) """

import json

def main():

    # create a simple JSON array
    jsonString = '{"key1":"value1","key2":"value2","key3":"value3"}'

    # change the JSON string into a JSON object
    jsonObject = json.loads(jsonString)

    # print the keys and values
    for key in jsonObject:
        value = jsonObject[key]
        print("The key and value are ({}) = ({})".format(key, value))

    pass

if __name__ == '__main__':
    main()