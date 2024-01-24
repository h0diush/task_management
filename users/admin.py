from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    change_user_password_template = None

    fieldset = (
        (None, {'fields': (
            'username', 'email', 'phone_number',
        )}),
        (_('Личная информация'), {'fields': (
            'first_name', 'last_name'
        )}),
        (_('Permissions'), {'fields': (
            'is_active', 'is_staff', 'is_superuser'
        )})
    )
    list_display = ('id', 'full_name', 'email', 'phone_number')
    list_filter = ('id', 'is_superuser', 'is_active')
    list_display_links = ('id', 'full_name')
    search_fields = (
        'first_name', 'last_name', 'email', 'phone_number', 'username')
    ordering = ('-id',)
    filter_horizontal = ('groups', 'user_permissions')
    readonly_fields = ('last_login', 'date_joined')
