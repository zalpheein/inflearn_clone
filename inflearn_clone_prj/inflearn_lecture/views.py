from django.shortcuts import render
from .models import myText

def home_list(request):

    texts = myText.objects.filter(category='HTML')
    return render(request, 'inflearn_lecture/home_list.html', {
        'texts':texts
    })
