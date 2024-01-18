# 자율주행자동차 클래스 생성 - 상속 적용하기
# - 상속 적용하기
import ex_class_02 as e2

class AutoCar(e2.Car):
    def __init__(self, wheel, color, number, kind):
        super().__init__(wheel, color, number, kind)


    def auto(self,aimodel):
        print(f'ai 모델 {aimodel}의 활약으로 자율주행이 가능하다')


    # 자율비행자동차 클래스 생성
    # - 상속 적용하기
c1=AutoCar(12,'black','9344','테슬라')
c1.auto('시리')


class AutoFly(AutoCar):
    def __init__(self, wheel, fly, color, number, kind):
        super().__init__(wheel, color, number, kind)
        self.fly = fly


    def flying(self,modnum):
        print(f'{self.fly}사의 {modnum}날개를 장착한 차량은 자율비행이 가능하다')


c2=AutoFly(12,'Ikaros','black','9344','apple')
c2.flying('Fly to Sky')
c2.auto('스카이넷')




