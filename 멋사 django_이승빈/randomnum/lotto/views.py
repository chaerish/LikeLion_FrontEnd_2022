from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    num = request.GET.get("num")

    list = []
    for i in range(1,45):
        list.append(i)
    
    l = []
    for i in range(int(num)):
        s = random.sample(list,7)
        l.append(s)
        

   
    return render(request, 'result.html', {"num":num,"list":l})

    