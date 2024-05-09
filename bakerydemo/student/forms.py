# forms.py
from django import forms
from .models import MoodCheckSubmission

class MoodCheckForm(forms.ModelForm):
    class Meta:
        model = MoodCheckSubmission
        fields = ['happiness_level', 'energy_level', 'additional_notes', 'self_rating', 'mood_status']
