from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'submitted_at', 'answer_text')
    search_fields = ('name', 'question_text', 'answer_text')
