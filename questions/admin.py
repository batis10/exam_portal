from django.contrib import admin
from .models import Question, Option, QuestionTag, QuestionTagMap

class OptionInline(admin.TabularInline):
    model = Option
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'exam', 'question_type', 'difficulty', 'marks')
    list_filter = ('question_type', 'difficulty')
    search_fields = ('question_text',)
    inlines = [OptionInline]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'option_text', 'is_correct')
    list_filter = ('is_correct',)


@admin.register(QuestionTag)
class QuestionTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(QuestionTagMap)
class QuestionTagMapAdmin(admin.ModelAdmin):
    list_display = ('question', 'tag')
    list_filter = ('tag',)

