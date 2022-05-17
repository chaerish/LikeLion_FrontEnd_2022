from django.shortcuts import render
import random

# Create your views here.

#로또 함수   
# 요청이 들어왔을때, index.html을 보여줘라는 함수 
# 언제 실행할지는 url.py에 정의
#템플릿과 뷰 연동하기 위해서 render 함수 씀 
def lottoStart(request):
        return render(request,'index.html') 


#로또 결과 화면 

def lotto(request):
    if request.method=="GET": #get 요청이 들어와쓰면 
        num_lotto=int(request.GET['num_lotto'])#request로 받은 넘버값이 넘로또값이고,

        lotto_list=[] #빈 리스트 생성

        for i in range(0,num_lotto):
            pick=random.sample(range(1,46),5)
            pick.sort()
            lotto_list.append(pick)
        
        data={
                 'num_lotto':num_lotto,
                 'lotto_list':lotto_list
             }

        return render(request,'result.html',data)
        