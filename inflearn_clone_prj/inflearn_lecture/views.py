from django.shortcuts import render
from .models import myText

def home_list(request):

    #texts = myText.objects.filter(category='HTML')
    texts = myText.objects.filter()
    return render(request, 'inflearn_lecture/home_list.html', {
        'texts':texts
    })

def lecture_list(request):
    texts = myText.objects.filter()

    hot_lecture = myText.objects.filter(category='인기')


    return render(request, 'inflearn_lecture/lecture_list.html', {
        'texts':texts,
        'hot_lecture':hot_lecture,
    })


def login(request):


    return render(request, 'inflearn_lecture/login.html')




def join(request):


    return render(request, 'inflearn_lecture/join.html')








