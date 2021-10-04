from django.contrib import auth
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import myText, Comment
from .form import LectureForm



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
    print("lecture_list_info() : ", board_contents)

    comments = Comment.objects.filter(lecture=board_contents)
    print('Comments : ', comments)

    if request.user.is_authenticated:
        print('이게 뭘까?')
        print(request.user.username)

    if request.method == "POST":
        rate = request.POST['rate']
        writer = request.POST['writer']
        comment = request.POST['comment']

        Comment.objects.create(lecture=board_contents, 
                                rate=rate, 
                                writer=writer, 
                                comment=comment)

        return redirect('/lecture_list/' + str(pk))

    return render(request, 'inflearn_lecture/lecture_list_info.html', {
        'board_contents': board_contents, 
        'comments': comments,
    })


def show_lecture(request, pk):
    
    board_contents = get_object_or_404(myText, pk=pk)


    return render(request, 'inflearn_lecture/show_lecture.html', {
        'board_contents': board_contents, 
    })


def create_lecture(request):
    
    if request.method == "POST":
        #form = LectureForm(request.POST, request.FILES)
        form = LectureForm(request.POST)
        if form.is_valid():
            myText = form.save(commit=False)
            myText.author = request.user
            myText.save()

            return redirect('/')

    lecture_form = LectureForm()

    return render(request, 'inflearn_lecture/create_lecture.html', {
        'lecture_form': lecture_form,
    })


def edit_lecture(request, pk):
    
    lecture = get_object_or_404(myText, pk=pk)


    if request.method == "POST":
        #lecture_form = LectureForm(request.POST, request.FILES, instance=lecture)
        lecture_form = LectureForm(request.POST, instance=lecture)

        if lecture_form.is_valid():
            lec = lecture_form.save(commit=False)
            lec.author = request.user
            lec.save()

            return redirect('/my_lecture')
    else:
        lecture_form = LectureForm(instance=lecture)

    return render(reqauest, 'inflearn_lecture/edit_lecture.html', {
        'lecture_form': lecture_form,
        'primary_key': pk,
    })



def my_lecture(request):
    
    print(request.user)
    lectures = myText.objects.filter(author=request.user)

    return render(request, 'inflearn_lecture/my_lecture.html', {
        'lectures': lectures,
    })


def comment_remove(request, pk):
    
    if request.method == "POST":
        Comment.objects.get(pk=pk).delete()
    
    return redirect('/lecture_list')



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








