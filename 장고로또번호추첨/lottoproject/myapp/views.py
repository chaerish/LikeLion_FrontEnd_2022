import random
from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request, 'input.html')

def result(request):
    lotto =[]
    game = int(request.GET['lotto_game'])
    for i in range (game):
        lotto_number =random.sample(range(1,46),6)
        lotto.append(lotto_number)
    

    context ={ 'lotto' : lotto,
                'game' : game}
    
    return render(request, 'result.html', context)    

def hello(request):
    return render(request, 'index.html')    