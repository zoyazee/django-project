from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
	list_display = ("name","duration_in_months","start_date","end_date",)
	search_fields = ("name","duration_in_months","start_date","end_date","teacher__first_name",)

admin.site.register(Course,CourseAdmin)


# Register your models here.
