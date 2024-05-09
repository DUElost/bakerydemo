from django.db import models
from django.contrib.auth.models import User
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField


# Create your models here.
class EmotionRecord(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_emotion_records')
    date = models.DateField()
    emotion_level = models.IntegerField()
    event = models.TextField()


# class MoodHomePage(Page):
#     body = RichTextField(blank=True)
#
#     content_panels = Page.content_panels + [
#         FieldPanel('body', classname="full"),
#     ]
#     parent_page_types = []
#     subpage_types = []


class MoodCheckSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submit_time = models.DateTimeField(auto_now_add=True)
    happiness_level = models.IntegerField(null=True, blank=True)
    energy_level = models.IntegerField(null=True, blank=True)
    feel_result = models.CharField(max_length=100, null=True, blank=True)
    additional_notes = models.TextField(blank=True, null=True)
    self_rating = models.IntegerField(null=True, blank=True)
    mood_status = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['-submit_time']

    def __str__(self):
        return f"{self.user.username} - {self.submit_time}"


class MoodCheckRecordPage(AbstractForm):
    # 在此处定义任何额外的字段或方法

    # 配置表单字段在管理后台中的显示方式
    content_panels = AbstractForm.content_panels + [
        # 在此处添加您的表单字段
    ]


class FormField(AbstractFormField):
    page = ParentalKey(MoodCheckRecordPage, on_delete=models.CASCADE, related_name='form_fields')
