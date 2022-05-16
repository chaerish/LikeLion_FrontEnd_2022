from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.
def home(request):
   return render(request, 'index.html')

def test(request):
   return render(request, 'test.html')

def lotto(request):
   return render(request, 'lotto.html')

def result(request):
   if request.method == 'GET':
      count = request.GET['count']
   
   lotto_lists = []
   for _ in range(int(count)):
      list = random.sample(range(1, 45), 6)
      lotto_lists.append(list)
   
   data = {
      'list': lotto_lists,
      'count': count
   }

   return render(request, 'result.html', data)
