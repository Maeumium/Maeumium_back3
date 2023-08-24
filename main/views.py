from django.shortcuts import render, redirect, get_object_or_404
from .models import Diary
from .forms import DiaryForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse



def couple_diary(request):
    latest_diary = Diary.objects.last()  # 가장 최근에 추가된 일기 가져오기
    if not latest_diary:  # 일기가 없다면
        latest_diary = None  # None 값을 설정합니다.
    return render(request, 'main/couplediary.html', {'diary': latest_diary})

def my_diary(request):
    return render(request, 'main/mydiary.html')

def writing(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        emotion = request.POST['emotion']
        privacy = request.POST['privacy']
        thumbnail = request.FILES.get('thumbnail')

        diary = Diary(title=title, content=content, emotion=emotion, privacy=privacy, thumbnail=thumbnail)
        diary.save()

        response_data = {'redirect_url': reverse('main:couple_diary')}
        return JsonResponse(response_data)

    return render(request, 'main/write.html')