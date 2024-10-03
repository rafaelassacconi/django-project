
# Docs: 
# - Model Admin Example: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#modeladmin-objects
# - Model Inline: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.StackedInline
# - search_fields: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
# - list_filter: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/filters/#modeladmin-list-filters
# - list_display: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display

from django.contrib import admin
from .models import Question, Option, Vote

class OptionInline(admin.TabularInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
     inlines = [OptionInline]
     list_display = ['text', 'options', 'created_at', 'enabled']
     list_filter = ['enabled']
     search_fields = ['text']

     def options(self, obj):
          return obj.option_set.count()

class VoteAdmin(admin.ModelAdmin):
     list_display = ['option__question', 'option', 'created_at']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Vote, VoteAdmin)
