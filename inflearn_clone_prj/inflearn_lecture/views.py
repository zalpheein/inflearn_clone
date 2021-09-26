from django.shortcuts import render

def home_list(request):
    return render(request, 'inflearn_lecture/home_list.html')
