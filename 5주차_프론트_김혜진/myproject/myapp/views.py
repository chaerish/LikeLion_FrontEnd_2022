from django.shortcuts import render
from django.db import models
import random
# Create your views here.


def home(request):
    
    return render(request, 'lotto.html')

def home2(request):

    if request.method == "GET":
        count = int(request.GET['count'])

    lotto = []
    lotto_2 = []

    for i in range(count):
        lotto = random.sample(range(1, 46), 6)
        lotto.sort()
        lotto_2.append(lotto)
        
    data = {
        'count' : count,
        'result' : lotto_2
        }

    return render(request, 'result.html', data)


    