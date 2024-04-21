from django.shortcuts import render

# Create your views here.
from .models import EmotionRecord

def emotion_record(request):
    records = EmotionRecord.objects.filter(student=request.user)
    return render(request, 'student/emotion_record.html', {'records': records})