from django.shortcuts import render
from django.http import HttpResponse

from model import GPT2PPL

model = GPT2PPL()

def checker(request):
    return render(request, 'index.html')

def formInput(request):
    text = request.POST.get('inputText', '')
    result, label, mean_prob = model(text, 100)
    print(result, label, mean_prob)
    return render(request, 'index.html', {'result': result, 'label': label, 'mean_prob': mean_prob})
