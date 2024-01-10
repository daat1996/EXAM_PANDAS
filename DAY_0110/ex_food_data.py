file = 'food.txt'

kor_food, china_food = [], []
foods = {}
kind = ''
# with open(file, mode='r', encoding='utf8') as f:
#     data = f.readline()
#     if not data.index('*'):
#         kind = '한식' if data[1:] == '한식' else '중식'
#     else:
#         if kind == '한식': kor_food.append(data)
#         else:
#             china_food.append(data)

key = ''
with open(file, mode='r', encoding='utf8') as f:
    data = f.readline()
for mas in data:
    if not data.find('*'):
        kind = data[1:]
        foods[data[1:]]=[]
    else:
        print(foods[key].append(data))
print(foods)