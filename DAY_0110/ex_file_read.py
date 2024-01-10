# --------------------------------------------------------------------------------
# 파일 입출력, => 출력 즉 읽기(Read)
# - 사용 내장함수 : oepn(file, mode='rt[기본]', encoding = '시스템기본기')
# - encoding 설정 : 파일에 적용된 인코딩을 설정해야 함!!
# --------------------------------------------------------------------------------
# (1) open

file = open('message.txt', encoding='utf8')     # 파일에 인코딩된 형식과 같은 것으로 써야함
print(f'file => {type(file)}, {file}')      # IO는 입력/출력 을 뜻한다.

# (2) 10 = read() : 파일 안에 모든 내용 다 읽어오기
# fdata = file.read()
# print(f'fdata => {type(fdata)}, {fdata}')


# (2) IO => read(n) : 지정된 숫자 만큼 문자를 파일에서 읽어오기
# fdata = file.read(5)        # 지정된 숫자 만큼 문자 읽기 -> 여기서는 5개 읽어라(공백도 포함되어 있다)
# print(f'fdata => {type(fdata)}, {fdata}')
#
# fdata = file.read(5)        # 5개만 나옴: 5바이트
# print(f'fdata => {type(fdata)}, {fdata}')

# (2) IO => readline(n) : '\n'기준으로 한 줄 읽어오기
# datas = []
# while True:
#     fline = file.readline()
#     if not fline: break
#     print(f'file => {type(fline)}, {fline}', end='')
#     datas.append(fline)
# (2) IO => readlines() : '\n'기준으로 한 줄 씩 읽은 것을 리스트에 담아서 반환
datas = file.readlines()

print(datas)

#(3) close
file.close()
