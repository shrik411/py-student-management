from django.contrib import admin
from .models import Lecture

# Register your models here.

class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecture_name', 'date')
    search_fields = ('title', 'lecture_name')


admin.site.register(Lecture, LectureAdmin)
