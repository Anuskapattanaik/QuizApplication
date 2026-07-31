from django.contrib import admin
from .models import Question, Option, UserProfile

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ('text', 'category')
    list_filter = ('category',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(UserProfile)
admin.site.register(Option)
