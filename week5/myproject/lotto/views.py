from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'index.html')

def result(request):
    lotto=[]
    count=int(request.GET['count'])
    for i in range(count):
        number=random.sample(range(1,46),6)
        lotto.append(number)
    result={"lotto" : lotto, 'count':count}
    return render(request,'result.html',result)