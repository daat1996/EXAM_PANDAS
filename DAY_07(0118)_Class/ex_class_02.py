# ----------------------------------------------------------------------------
# 자동차 클래스
# 클래스 이름 : Car
# 클래스속성 : 바퀴, 색상, 차번호, 차종류(인스턴스 속성), 제조사(클래스 속성)
# 클래스기능 : 주행한다, 정지한다, 후진한다
# ----------------------------------------------------------------------------
class Car:
    # 클래스 속성
    maker='현대'

    # 생성자 메서드 => 객체 즉, 인스턴스 생성 메서드
    def __init__(self, wheel, color, number, kind):
        #힙 영역에 저장
        self.wheel=wheel
        self.color=color
        self.number=number
        self.kind=kind

    # 객체 즉, 카 인스턴스 메서드
    def driving(self, where):
        print(f'{where}에 {self.number}차가 드라이빙하고 있다.')

    def stop(self, place):
        print(f'{self.number} 차가 {place}에 정지 한다.')

    def back(self):
        print(f'{self.number} 차가 후진 한다.')

# -------------------------------------------------------------------------
# 자동차 인스턴스 생성
# -------------------------------------------------------------------------
myCar=Car(19,'red','1111','새단')
secondCar=Car(20,'hotpink','7777','SUV')






# -------------------------------------------------------------------------------------
# 사랑 클래스
# 클래스 이름 : Love
# 클래스속성 : kind
# 클래스기능 : 새우까주기, 깻잎떼주기, 금융치료하기, 데려다주기, 데이트하기, 같이아프기
#              대신죽어주기, 희생하기
# --------------------------------------------------------------------------------------

class Love:

    # 생성자 메서드 => 객체 즉, 인스턴스 생성 메서드
    who = '연인'
    def __init__(self, kind):
        #힙 영역에 저장
        self.kind = kind

    def shrimp(self,num):
        print(f'새우를 {num}개 까준다')

    def leap(self,num):
        print(f'깻잎을 {num}개 떼준다')

    def money(self,price):
        print(f'{price}의 금액으로 행복하게 해준다')

    def carry(self,place,how):
        print(f'{place}까지 {how} 데려다준다')


# myLove=Love('연애')



# -------------------------------------------------------------------------------------
# 계산기 클래스
# 클래스이름 : Calc
# 클래스속성 : 브랜드, 종류, 색상, 크기, 가격
# 클래스기능 : 덧셈, 뺄셈, 곱셈, 나눈셈
# - 데이터 => 속성 또는 기능에서 매개변수
# --------------------------------------------------------------------------------------
class Calc:
    # 클래스 변수
    maker='카시오'
    __size=(7,15)             # 비공개 속성  __속성명 : 클래스 밖에서 속성 읽거나/쓰기 불가
    # 객체 즉 인스턴스 생성 메서드
    def __init__(self, kind, color, price, info):

        self.kind = kind
        self.color = color
        self.__info = info        # 인스턴스 생성 시 계산기에 각인되는 정보
        self.price = price
        self.data=0


    # 비공개 인스턴스 속성 읽기/쓰기(getter/setter) 메서드
    def getInfo(self):
        return self.__info

    def setInfo(self, info):
        self.__info=info


    # 비공개 인스턴스 속성 읽기/쓰기(getter/setter) 메서드
    # => 속성 읽기/쓰기 방식으로 동작하도록 설정
    @property
    def info(self): return self.__info


    @info.setter
    def info(self,info):
        self.__info=info

    def plus(self, nums):
        self.data += nums

    def minus(self, nums):
        self.data -= nums

    def multi(self, nums):
        self.data *= nums

    def div(self, nums):
        if not nums: return '0으로 나눌 수 없습니다.'
        self.data = self.data/nums

    def result(self):
        return self.data


# -------------------------------------------------------------------------------
# Calc 클래스로 인스턴스 생성 => 힙에 생성 :인스턴스 변수 +클래스 변수 다 확인 가능
#                                           인스턴스 메서드 사용 가능
# -------------------------------------------------------------------------------
c1=Calc('공학용','블랙',10000, '만상')


# 인스턴스 속성 읽기 => 공개 속성만 읽기 가능
# print(c1.data, c1.color, c1.kind)
#
# # 인스턴스 속성 변경 => 공개 속성만 읽기 가능
# c1.color='빨강색'
#
# # 인스턴스 비공개 속성 읽기 ==> 전용에 메서드 getter/setter 통해서 읽기/쓰기
# print(c1.getInfo(), c1.info)
#
# # 인스턴스 비공개 속성 변경 ==> 전용에 메서드 getter/setter 통해서 읽기/쓰기
# c1.setInfo('내꺼')
# c1.info='내꺼야~~'
#
#
# print(c1.getInfo(), c1.info)


# -------------------------------------------------------------------------------
# Calc 클래스로 계산기 정보 확인 => 클래스 변수만 확인 가능
#                                   인스턴스 변수나 메서드 사용 불가능!!
#                                   self 값이 없음!
# -------------------------------------------------------------------------------

# print(Calc.maker)


# 인스턴스 메서드에 접근 불가!!
#print(Calc.plus(10))       # self로 들어가서 에러난다