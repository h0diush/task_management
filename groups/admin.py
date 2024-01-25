from django.contrib import admin

from groups.models.groups import Group, Employee


class EmployeeInline(admin.TabularInline):
    model = Employee
    fields = ('user', 'date_joined',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'administrator')
    search_fields = ('name', 'administrator')
    inlines = (EmployeeInline,)
