file = 'food.txt'

kor_food, china_food = [], []
foods = {}
kind = ''
with open(file, mode='r', encoding='utf8') as f:        # 1. 리스트 만들어서 분류하는법
    while True:
        data = f.readline().replace('\n','')
        if not data:
            break
        if not data.find('*'):
            kind = '한식' if data[1:] == '한식' else '중식'
        else:
            if kind == '한식': kor_food.append(data)
            else:
                china_food.append(data)

print(kor_food)
print(china_food)

key = ''
with open(file, mode='r', encoding='utf8') as f:        # 2. 딕셔너리로 정리하는 법
    datas = f.readlines()
print(datas)
for mas in datas:
    mas = mas.replace('\n','')
    if not mas.find('*'):
        key = mas[1:]
        foods[key]=[]
    else:
        foods[key].append(mas)
        print(foods)
print(foods)

