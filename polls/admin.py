from django.contrib import admin

from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

# Customize the admin class to control the form
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    # Add Choices while creating a new question
    inlines = [ChoiceInLine]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    # Search field uses LIKE therefore, be judicious with # of fields included
    search_fields = ["question_text"]

# Register your models here.
admin.site.register(Question, QuestionAdmin)