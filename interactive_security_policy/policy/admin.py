from django.contrib import admin
from policy.models import Policy

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
