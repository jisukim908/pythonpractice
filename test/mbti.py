def you(name, mbti) :
    a= name.strip()
    b= (mbti.strip()).upper()
    print(f'{a}의 mbti는 {b}이다.')

    #if b in 'E':
    #    print(f'{a}님은 지금 신나게 수다떨면서 놀고 싶다. 혼자 있기 싫다.')
    #else:
    #    print(f'{a}님은 지금 집에 가고 싶다. 넷플릭스를 보며 혼자만의 시간을 갖고 싶다.')

    result = ('지금 신나게 수다 떨면서 놀고 싶다. 혼자 있기 싫다.' if b in 'E'
              else '지금 집에 가고 싶다. 넷플릭스를 보며 혼자만의 시간을 갖고 싶다.')
    print(f'{a}님은 {result}')

name = str(input("이름을 적어주세요."))
mbti = str(input("mbti를 적어주세요."))

you(name,mbti)
