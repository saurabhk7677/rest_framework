from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
class AccountAdmin(BaseUserAdmin):

    list_display = ('email', 'first_name', 'last_name', 'phone', 'date_of_birth', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'password',)}),
        ('Personal info', {'fields': ('phone', 'date_of_birth')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions', )}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'password1', 'password2',)}),
        ('Personal info', {'fields': ('phone', 'date_of_birth')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions', )}),
    )

    search_fields = ('email', 'name', 'phone',)
    readonly_fields = ('password_hint',)
    # filter_horizontal = ('groups', 'userpermissions', )

admin.site.register(User, AccountAdmin)
