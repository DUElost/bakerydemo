# Create your views here.
from .models import EmotionRecord
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MoodCheckSubmission, MoodCheckRecordPage
from wagtail.contrib.forms.models import FormSubmission
from django.contrib.auth.models import User


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


def personal_history(request):
    user = request.user
    return render(request, 'student/personal.html')


def myclass_view(request):
    # 获取所有用户对象
    users = User.objects.all()

    # 将用户对象列表传递给模板
    context = {
        'users': users
    }

    return render(request, 'student/myclass.html', context)


# views.py
@login_required
def wellness_view(request):
    if request.method == 'POST':
        happiness_level = request.POST.get('happiness_level')
        energy_level = request.POST.get('energy_level')
        submission, created = MoodCheckSubmission.objects.get_or_create(
            user=request.user,
            defaults={'happiness_level': happiness_level, 'energy_level': energy_level}
        )
        if not created:
            submission.happiness_level = happiness_level
            submission.energy_level = energy_level
            submission.save()
        return redirect('mood_check_view')
    return render(request, 'student/wellness.html')


@login_required
def mood_check_view(request):
    user = request.user
    submission, created = MoodCheckSubmission.objects.get_or_create(user=request.user, feel_result__isnull=True)
    if request.method == 'POST':
        feel_result_list = request.POST.getlist('feel_result')
        feel_result = ', '.join(feel_result_list)  # 将列表转换为字符串
        submission.feel_result = feel_result
        submission.save()
        return redirect('mood_check_record_view')
    return render(request, 'student/mood_check.html', {'submission': submission})


@login_required
def mood_check_record_view(request):
    submission = get_object_or_404(MoodCheckSubmission, user=request.user, additional_notes__isnull=True)
    # 获取 MoodCheckRecordPage 实例
    page = MoodCheckRecordPage.objects.live().first()

    if request.method == 'POST':
        form = page.get_form(request.POST, page=page, user=request.user)
        if form.is_valid():
            # 从表单中获取数据
            additional_notes = form.cleaned_data.get('additional_notes')
            self_rating = form.cleaned_data.get('self_rating')
            mood_status = form.cleaned_data.get('mood_status')

            # 更新 MoodCheckSubmission 对象
            submission.additional_notes = additional_notes
            submission.self_rating = self_rating
            submission.mood_status = mood_status
            submission.save()

            # 执行其他操作,例如重定向等
            return redirect('mood_check_history')
    else:
        form = page.get_form(page=page, user=request.user)

    return render(request, 'student/mood_check_record.html', {
        'form': form,
    })


@login_required
def mood_check_history(request):
    submissions = MoodCheckSubmission.objects.filter(user=request.user)
    return render(request, 'student/mood_check_history.html', {'submissions': submissions})


@login_required
def form_submissions_view(request):
    found_data = False
    form_submissions = FormSubmission.objects.all()
    return render(request, 'student/mood_check_history.html',
                  {'form_submissions': form_submissions})
