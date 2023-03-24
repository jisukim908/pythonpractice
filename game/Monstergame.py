import random
import time

#엄마몬스터 클래스: 기본값들 설정 .. 예를 들어  hp, 공격 받는 거, healing들..
#악당 몬스터
#불몬스터, 물몬스터


class Monster():
    def __init__(self,hp):
        self.hp=hp

    def attack(self,damage):
        self.hp -= damage

    def healing(self,plus):
        self.hp += plus
        print(f'치유스킬 발동. 남은 hp : {self.hp}')

    def status_check(self):
        if self.hp > 0:
            print(f'마왕이 반격을 했다. 당신의 몬스터는 살았습니다. 남은 hp : {self.hp}')
        else:
            print(f'마왕이 반격을 했다. 당신의 몬스터는 죽었습니다.')

class EvilMonster(Monster):
    def __init__(self,hp):
        super().__init__(hp)

    def status_check(self):
        if self.hp>0:
            print(f'당신의 몬스터가 공격을 했다. 마왕 hp : {self.hp}')
        else:
            print('용사여 승리하였습니다.')

class FireMonster(Monster):
    def __init__(self,hp):
        self.attribute = "fire"
        super().__init__(hp)

class WaterMonster(Monster):
    def __init__(self,hp):
        self.attribute = "water"
        super().__init__(hp)


print("용사여 환영합니다. 당신은 마왕을 무찔러야 합니다. 당신의 몬스터를 고르세요.")
time.sleep(2)
print("물몬스터(w)는 공격데미지가 상대적으로 높습니다. 불몬스터(f)는 치유력 회복이 느립니다.")
time.sleep(2)
choice = input("당신의 선택은? w 또는 f 중 하나를 써주세요.").strip()
print("당신의 몬스터가 공격을 시작합니다.")
time.sleep(2)
if choice == "w":
    evil = EvilMonster(hp=100)
    water = WaterMonster(hp=100)
    while evil.hp>0 and water.hp>0:
        evil.attack(damage=int(random.randint(1, 40)))
        evil.status_check()
        if evil.hp<0:
            break
        else:
            evil.healing(plus=random.randint(1, 15))
        time.sleep(2)
        water.attack(damage=int(random.randint(10, 40)))
        water.status_check()
        if water.hp<0:
            break
        else:
            water.healing(plus=random.randint(1, 20))
        time.sleep(2)
elif choice == "f":
    evil = EvilMonster(hp=100)
    fire = FireMonster(hp=100)
    while evil.hp > 0 and fire.hp > 0:
        evil.attack(damage=int(random.randint(1, 40)))
        evil.status_check()
        if evil.hp < 0:
            break
        else:
            evil.healing(plus=random.randint(1, 15))
        time.sleep(2)
        fire.attack(damage=int(random.randint(1, 40)))
        fire.status_check()
        if fire.hp<0:
            break
        else:
            fire.healing(plus=random.randint(1, 10))
        time.sleep(2)
else:
    print("잘못 입력하셨습니다.")


