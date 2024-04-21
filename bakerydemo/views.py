from django.shortcuts import render

# Create your views here.
#个人信息
def student_homepage(request):
    # AUTH_USER_MODEL 类型的对象，表示当前登录的用户。
    user = request.user
    return render(request, 'main_home/student_homepage.html')