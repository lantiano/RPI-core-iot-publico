""" import json

input_dict = {'foo': 3, 'bar': 1}
result = []

for k, v in input_dict.items():
    result.append({'key': k, 'value': v})

print(json.dumps(result)) """

""" import json

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
    main() """

""" import csv
import json
import os

#simp_path = '19-01-2022.csv'
#bs_path = os.path.abspath(simp_path)

#print(abs_path)


#file = abs_path
file = '19-01-2022.csv'
json_file = 'output_file_name.json'

#Read CSV File
def read_CSV(file, json_file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        convert_write_json(csv_rows, json_file)

#Convert csv data into json
def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))) #for pretty
        f.write(json.dumps(data))


read_CSV(file,json_file)  """

""" import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files)) """

""" import os

simp_path = '19-01-2022.csv'
abs_path = os.path.abspath(simp_path)

print(abs_path)
 """

""" import csvmapper

fields = ('Hora', 'Valor')
parser = CSVParser('2columnas.csv', csvmapper.FieldMapper(fields))

converter = csvmapper.JSONConverter(parser)

print (converter.doConvert(pretty=True)) """

""" import csv

with open('2columnas.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)  """

import csv
file = open("2columnas.csv")

reader = csv.reader(file)

lines= len(list(reader))
print(lines)
my_list = []

with open('2columnas.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        my_list.append(row)

    with open('2columnas.json', 'w') as f:
        #f.write(','.join(my_list))
        f.write(str(my_list))

    print(my_list)
    #lines = ['Readme', 'How to write text files in Python']
        
    #with open(my_list, 'w') as f:
        #f.write(','.join(lines))
    

""" def writing_ArryJson():

        lines = ['Readme', 'How to write text files in Python']
        
        with open('readme.txt', 'w') as f:
            f.write('\n'.join(lines))
    
        with open('2columnas.json') as csvfile:
            employee_writer = csv.writer(csvfile)
            employee_writer.writerow(['dia', 'seg', 'hora', 'P1', 'P2', 'P3', 'P4', 'E1', 'E2', 'E3', 'E4', 'mil'])
 """


""" for i in range(lines):

	my_list.append("New Element")


print(a_list)
 """


""" # Create an empty list
my_list = []
values1 = [32, 748, 125, 458, 987, 361]
my_list.append(values1)
#print(my_list)

values2 = [42, 344, 145, 448, 187, 304]    
my_list.append(values2)
print(my_list) """