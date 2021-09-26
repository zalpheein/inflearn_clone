


# 저작권이 없는 무료 이미지 사이트
https://www.unsplash.com


# 한글입숨 - 한글 텍스트 생성기
http://hangul.thefron.me/


# 지정한 크기의 특정 또는 램덤 이미지를 가져오기
사용법 - https://www.designlog.org/2512699
https://picsum.photos/
	https://picsum.photos/200/300
	https://picsum.photos/200/300.jpg
	https://picsum.photos/id/237/200/300
	https://picsum.photos/200/300?grayscale
	https://picsum.photos/200/300/?blur
	https://picsum.photos/200/300/?blur=2
	https://picsum.photos/id/870/200/300?grayscale&blur=2
	https://picsum.photos/v2/list




---------------------------------------------------------------------------------



## 가상 환경 생성
    conda create -n inflearn_clone python~=3.9

# 장고 패키지 설치
django
pylint
django-ckeditor


## git 관리 폴더 생성
    "git clone 주소" 명령을 사용하여 git 관리 할 폴더 생성 
        	git clone https://github.com/zalpheein/inflearn_clone.git
        inflearn_clone 라는 git 전용 관리 폴더가 생성

            inflearn 폴더
            ㄴ inflearn_clone				<--- git 에서 생성한 git 전용 관리 폴더


## 장고 프로젝트 생성
    해당 폴더 내부에 장고 프로젝트 생성
        django-admin startproject inflearn_clone_prj 

            inflearn 폴더
            ㄴ inflearn_clone				<--- git 에서 생성한 git 전용 관리 폴더
               ㄴ inflear_clone_prj			<--- django-admin startproject 에서 생성한 폴더
               	ㄴ  inflear_clone_prj		<---		프로젝트 생성하면서 자동으로 만들어진 폴더

## 장고 앱 생성
	inflear_clone_prj 장고 프로젝트 폴더 내에서 django-admin startapp inflearn_lecture 라는 장고앱 생성

            inflearn 폴더
            ㄴ inflearn_clone				<--- git 에서 생성한 git 전용 관리 폴더
               ㄴ inflear_clone_prj			<--- django-admin startproject 에서 생성한 폴더
               	ㄴ inflear_clone_prj		<---		프로젝트 생성하면서 자동으로 만들어진 폴더
               	ㄴ inflearn_lecture			<--- 장고 앱


## DB 마이그래이션 & 마이그레이트 & 슈퍼유저 생성
    zalphee / 2단계 비번
