from django.shortcuts import render

# Create your views here.
from .models import EmotionRecord


def emotion_record(request):
    records = EmotionRecord.objects.filter(student=request.user)
    return render(request, 'student/emotion_record.html', {'records': records})


def student_homepage(request):
    # AUTH_USER_MODEL 类型的对象，表示当前登录的用户。
    user = request.user
    return render(request, 'main_home/student_homepage.html')


def wellness(request):
    user = request.user
    return render(request, 'student/wellness.html')


def mood_check(request):
    user = request.user
    return render(request, 'student/mood_check.html')


def mood_check_history(request):
    user = request.user
    return render(request, 'student/mood_check_history.html')
