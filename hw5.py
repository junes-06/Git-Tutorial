def read_single_digit(n):
    if n==1:
        return '일'
    elif n==2:
        return '이'
    elif n==3:
        return '삼' 
    elif n==4:
        return '사'
    elif n==5:
        return '오'
    elif n==6:
        return '육'
    elif n==7:
        return '칠'
    elif n==8: 
        return '팔'
    elif n==9:
        return '구'
    elif n==0:
        return '영'
    

def read_number(number):
    for num in number:
        print(read_single_digit(int(num)), end='')
    print()   

number=input('세 자리 정수 입력:')
read_number(number)