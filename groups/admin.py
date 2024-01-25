from django.contrib import admin

from groups.models.groups import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'administrator')
    search_fields = ('name', 'administrator')
