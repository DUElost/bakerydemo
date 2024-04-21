from django.contrib import admin

# Register your models here.
from .models import EmotionRecord

admin.site.register(EmotionRecord)