from typing import Sequence
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.utils.translation import gettext as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display: Sequence[str] = (
        'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'last_login')
    list_filter: Sequence[str] = (
        'email', 'is_staff', 'is_active', 'date_joined', 'last_login')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('User Information'), {
         'fields': ('username', 'first_name', 'last_name')}),
        (_('Extra Information'), {
            'fields': ('date_of_birth', 'phone', 'photo', 'photo_preview')}),
        (_('Permissions'), {
         'fields': ('is_staff', 'is_active', 'is_superuser')}),
        (_('Groups'), {'fields': ('groups', 'user_permissions')}),
        (_('Meta'), {'fields': ('date_joined', 'last_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email',  'password1', 'password2',
                       'is_staff', 'is_active'
                       )}
         ),
    )
    search_fields: Sequence[str] = ('email',)
    ordering: Sequence[str] = ('email',)
    readonly_fields: Sequence[str] = (
        'username', 'date_joined', 'last_login',
        'date_of_birth', 'phone', 'photo_preview'
    )
    save_on_top: bool = True

    """
    Override the original get_readonly_fields method and
    update the readonly_fields.
    """

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('email', 'first_name', 'last_name')
        return super().get_readonly_fields(request, obj) + self.readonly_fields

    # Override the original get_actions method and prevent to delete the user.

    def get_actions(self, request):
        pass
