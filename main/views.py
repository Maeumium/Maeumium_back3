from django.shortcuts import render, redirect, get_object_or_404
from .models import Diary
from .forms import DiaryForm
from django.shortcuts import render, redirect


def couple_diary(request):
    latest_diary = Diary.objects.last()  # 가장 최근에 추가된 일기 가져오기
    if not latest_diary:  # 일기가 없다면
        latest_diary = None  # None 값을 설정합니다.
    return render(request, 'main/couplediary.html', {'diary': latest_diary})

def my_diary(request):
    return render(request, 'main/mydiary.html')

def writing(request):
    if request.method == "POST":
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('couple_diary')  # 저장 후 원하는 뷰로 리디렉션합니다.
    else:
        form = DiaryForm()
    return render(request, 'main/write.html', {'form': form})
