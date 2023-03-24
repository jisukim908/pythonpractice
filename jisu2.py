class JipsooniTest():
    like = 100
    alive = True

    def jip(self, hate):
        self.like = self.like - hate
        if self.like <40:
            self.alive = False

    def status_check(self,name):
        if self.alive:
            if self.like>60:
                print(f'{name}님은 진정한 집순이십니다. 환영해요 :)')
            else:
                print(f'{name}님! 집순이가 적성에 맞을지도 몰라~')
        else:
            print(f'죄송하지만.. {name}님께서는 집순이라 하실 수 없어요...ㅠ (숙연)')

def test(number,name):
    test1=JipsooniTest()
    test1.jip(number)
    test1.status_check(name)

hate = input("하루종일 집에만 있으면 어때? 싫은 정도를 0부터 100까지 숫자 중에 표현해줘~")
name = input("이름을 적어줘~")

test(int(hate), str(name))