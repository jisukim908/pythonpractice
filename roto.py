import time
from datetime import datetime, timedelta
import random
from pprint import pprint

#오늘 날짜의 로또 번호를 출력해주는 클래스
class TodayRottoTest():
    now=datetime.now()
    string_datetime = datetime.strftime(now,"%y/%m/%d")
    rotto_list = []
    for a in range(6):
        rotto = random.randint(1,45)
        rotto_list.append(rotto)
    name=input("안녕하세요. 당신의 이름을 입력해주세요.").strip()
    time.sleep(1)
    print(f'잠시 후 "{string_datetime}"의 로또 번호를 출력해드립니다.')
    time.sleep(1)
    print(f'{name}님의 로또 번호는 ...')
    time.sleep(2)
    print(f'{rotto_list}입니다.')

print(TodayRottoTest)
