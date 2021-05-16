


import json
import jsonpath

#loads(),将json数据转成dict数据
#load(),读取json文件数据，转成dict数据
with open('response.json', encoding="UTF-8") as f:
    load_dict=json.load(f)

print(load_dict)
print(type(load_dict))

# dump()，将dict数据转换为json数据后写入json文件
# dumps()，将dict数据转换为json数据
load_data=json.dumps(load_dict)
print(load_data)
print(type(load_data))

print(load_dict['data'][0]['config']['value'][0]['name'])
# print(jsonpath.jsonpath(load_dict, '$.data[0].config.value[0].name'))