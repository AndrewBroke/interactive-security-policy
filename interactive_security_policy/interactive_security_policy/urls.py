from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from policy.views import policy, index, UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('policy/<int:chapter_id>/', policy, name="policy"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', index, name="index"),
]
