from django.shortcuts import render
import random

def index(request):
    cafeteria = ["haru", "cow_gop"]
    xCafeteria = ["37.558486", "37.558715"]
    yCafeteria = ["126.935894", "126.935051"]
    select_cafeteria = random.choice(cafeteria)
    index_num = cafeteria.index(select_cafeteria)
    x = xCafeteria[index_num]
    y = yCafeteria[index_num]
    return render(request, 'index.html', {'cafeteria' : select_cafeteria, 'x' : x, 'y' : y})