from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
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

def lecture_list_info(request, pk):

    board_contents = get_object_or_404(myText, pk=pk)
    print(board_contents)

    return render(request, 'inflearn_lecture/lecture_list_info.html', {
        'board_contents': board_contents
    })




## 로그인
def login(request):
    print("로그인 시작")

    if request.method == "POST":
        print("로그인 시작 - POST")
        email = request.POST['email']
        pwd = request.POST['pwd']

        user = auth.authenticate(request, username=email, password=pwd)

        if user is None:
            print("회원가입된 사람이 아님.....")
            return redirect('/join')
        else:
            print("회원임... 로그인 처리 전...")
            auth.login(request, user)
            print("회원임... 로그인 처리 후...")
            return redirect('/')
    return render(request, 'inflearn_lecture/login.html')



## 로그 아웃
def logout(request):

    auth.logout(request)
    return redirect('/')



## 회원 가입
def join(request):

    print("join 실행")
    if request.method == "POST":
        print("여기는 포스트 요청")

        email = request.POST['email']
        pwd = request.POST['pwd']
        User.objects.create_user(username=email, password=pwd)

        return redirect('/')

    print("join 마지막 부분")
    return render(request, 'inflearn_lecture/join.html')








