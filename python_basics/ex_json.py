import json
# # 网络传输的时候只有字符串/字节，存储的时候可吧json做为对象存储；
# # json.dumps()将一个Python数据结构转换为json
# data = {
#     'name': 'ACME',
#     'shares': 100,
#     'price': 542.23
# }
#
# print(type(data))
# json_str = json.dumps(data)
#
# print(json_str)
# print(type(json_str))
#
# # json.loads()将一个JSON编码的字符串转换回一个Python数据结构
# data = json.loads(json_str)
# print(data)
# print(type(data))





with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)


