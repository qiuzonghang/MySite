from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):

    # 默认去MySite下templates找，然后去app下的templates目录下寻找user_list.html（根据app注册顺序去找）
    return render(request, "user_list.html")
