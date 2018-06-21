from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.html import format_html

from IncredibleBonds.forms import CustomUserCreationForm, CustomUserChangeForm
from IncredibleBonds.models import *
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Hemophilia)
admin.site.register(Patient)
admin.site.register(Parent)


class PatientInline(admin.StackedInline):
    model = Patient
    can_delete = False
    verbose_name_plural = 'Patient'


class ParentInline(admin.StackedInline):
    model = Parent
    can_delete = False
    verbose_name_plural = 'Parent'


class DoctorInline(admin.StackedInline):
    model = Doctor
    can_delete = False
    verbose_name_plural = 'Doctor'


class ProfileAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Profile
    list_display = ['email', 'username']


admin.site.register(Profile, ProfileAdmin)
