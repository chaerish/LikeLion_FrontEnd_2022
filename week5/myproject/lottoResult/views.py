from django.shortcuts import render
import random

# Create your views here.
def game(request):
    num = request.GET['number']

    my_lotto = [] #로또 한 게임
    total_lotto = [] #사용자가 입력받은 수 만큼 실행한 로또

    for i in range(int(num)):
        my_lotto = random.sample(range(1,46), 6)
        total_lotto.append(my_lotto)

    data = {
        'mynum' : num,
        'result' : total_lotto
    }

    return render(request, 'index2.html', data)
