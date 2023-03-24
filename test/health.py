#표준체중(kg) = (현재신장cm - 100) X 0.9
#비만도(%) = (현재체중 ÷표준체중) X 100

def inbody_check(func):
    def wrapper():
        weight = int(input("당신의 몸무게를 입력하세요."))
        height = int(input("당신의 키를 입력하세요."))
        func(weight,height)

    return wrapper

@inbody_check
def bmi_test(weight, height):
    a = round((height - 100)*0.9,2)
    b = round((weight/a)*100,2)
    print(f'당신의 키를 기준으로 표준체중은 {a}kg이고, 당신의 비만도는 {b}%입니다.')
    if b<80:
        print("당신은 심각한 저체중입니다.")
    elif b<90:
        print("당신은 약한 저체중입니다.")
    elif b<110:
        print("당신은 장싱체중입니다.")
    elif b<120:
        print("당신은 과체중입니다.")
    elif b<130:
        print("당신은 경도비만입니다.")
    elif b<150:
        print("당신은 중증도비만입니다.")
    elif b<200:
        print("당신은 고도비만입니다.")
    else:
        print("당신은 위험한 비만입니다.")

bmi_test()