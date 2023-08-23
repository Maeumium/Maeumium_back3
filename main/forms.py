# forms.py

from django import forms
from .models import Diary  # Diary 모델을 정의해야 함

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['privacy', 'emotion', 'title', 'content', 'thumbnail']
