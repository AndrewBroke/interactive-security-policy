from django.shortcuts import render
from django.contrib.auth.views import LoginView
from common.views import TitleMixin
from django.urls import reverse_lazy, reverse

from policy.models import Policy
from policy.forms import UserLoginForm


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
