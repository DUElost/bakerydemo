from django.db import models
from django.contrib.auth.models import User
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


# Create your models here.
class EmotionRecord(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE) 
    date = models.DateField()
    emotion_level = models.IntegerField()
    event = models.TextField()
    


class MoodHomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]