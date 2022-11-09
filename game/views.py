from django.shortcuts import render
import random
# Create your views here.

translate = {
        'rock': 'камень',
        'knife': 'ножницы',
        'paper': 'бумага'
    }

def index(request):
    return render(request, 'game/index.html')

def result(request):
    variants = ['rock', 'knife', 'paper']
    win = {
        'rock': 'knife',
        'knife': 'paper',
        'paper': 'rock'
    }
    choice = request.GET.get('choice')
    ai_choice = random.choice(variants)
    res = choice == ai_choice
    ind = 0
    if res:
        res = 'Ничья.'
    else:
        if win[choice] == ai_choice:
            res = "Вы победили!"
            ind = 1
        else:
            res = "Вы проиграли..."
            ind = 2
    return render(request, 'game/result.html', {'choice':translate[choice],'ai_choice': translate[ai_choice],'result': res, 'index': ind})