from django.contrib import admin

from works.models import jobs, tasks


@admin.register(jobs.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'deadline')


@admin.register(tasks.Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'doer', 'status')
