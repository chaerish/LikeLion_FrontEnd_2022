from django.shortcuts import render
import random

# Create your views here.
def lotto(request) :
    return render(request, 'index.html')

def result(request) :
    try : #예외 처리
        count = int(request.GET['count']) #count라는 파라미터를 받아 int형태로 저장
        mylotto = []
        while len(mylotto) < count : 
            lottoNumber = random.sample(range(1,46),6) #1~45 숫자 중에 6개 random으로 뽑기
            mylotto.append(lottoNumber)

        return render(request, 'result.html',{'count':count,'mylotto':mylotto})
        
    except ValueError :
        print('숫자를 입력하십시오!')
        return render(request, 'index.html')