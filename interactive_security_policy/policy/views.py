from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from common.views import TitleMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

from policy.models import Policy
from policy.forms import UserLoginForm, ChapterForm

from django.shortcuts import get_object_or_404


def policy(request, chapter_id ):
    context = {
        'title': 'Политика безопасности',
        'chapters': Policy.objects.all(),
        'chapter': Policy.objects.get(id=chapter_id)
    }
    return render(request, 'policy/index.html', context)


def index(request):
    context = {
        'title': 'Политика безопасности',
        'chapters': Policy.objects.all(),
        'chapter': Policy.objects.get(id=1)
    }
    return render(request, 'policy/index.html', context)


class UserLoginView(TitleMixin, LoginView):
    template_name = 'policy/login.html'
    title = 'Авторизация'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')

@login_required
def add_chapter(request):
    if request.method == 'POST':
        form = ChapterForm(data=request.POST)
        if form.is_valid():
            title = request.POST['title']
            text = request.POST['text']
            Policy.objects.create(title=title, text=text)
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = ChapterForm()

    context = {
        'title': 'Новая глава',
        'chapters': Policy.objects.all(),
        'form': form
    }
    return render(request, 'policy/new_chapter.html', context)
