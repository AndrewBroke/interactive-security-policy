from django.shortcuts import render
# from django.views.generic.base import TemplateView
# from common.views import TitleMixin

from policy.models import Policy

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

# class PolicyView(TitleMixin, TemplateView):
#     title = 'Политика безопасности'
#     template_name = 'policy/index.html'
