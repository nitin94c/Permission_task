from django.contrib import admin
from .models import FeedBack


@admin.register(FeedBack)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_by', 'created_time')
