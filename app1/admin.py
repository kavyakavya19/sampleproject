from django.contrib import admin
from .models import Student,Project,Team,Task,Status,Assignment
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Assignment)