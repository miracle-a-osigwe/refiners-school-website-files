from django.contrib import admin
from django.http.request import HttpRequest
from django.utils.html import format_html

from .models import (
    Student, Subject, Teacher, Class, Result, Section, Home, AboutUs, SchoolVision,
    CandidateInfo, CandidatePreviousSchool, ParentInfo
    )


class ReadOnlyAdminMixin:
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if obj:
            return True
        return False

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]

class ReadOnlyTabularInline(admin.TabularInline):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]

class PreviousSchoolInline(ReadOnlyTabularInline):
    model = CandidatePreviousSchool
    extra = 0

class ParentInline(ReadOnlyTabularInline):
    model = ParentInfo
    extra = 0

class CandidateInline(ReadOnlyTabularInline):
    model = CandidateInfo
    extra = 0

@admin.register(CandidateInfo)
class CandidateAdmin(admin.ModelAdmin, ReadOnlyAdminMixin):
    list_display = ['surname', 'firstName', 'dob', 'view_previous_schools', 'view_parents']
    # readonly_fields = ['surname', 'firstName', 'dob', 'view_previous_schools', 'view_parents']
    inlines = [PreviousSchoolInline, ParentInline]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def view_previous_schools(self, obj):
        return format_html("<br>".join([f"{ps.school_name} - {ps.date_history}" for ps in obj.candidate_previous_school.all()]))
    view_previous_schools.short_description = 'Previous Schools'

    def view_parents(self, obj):
        return format_html("<br>".join([f"{p.parent_surname} {p.parent_name} - {p.contact_number} ({p.email_address})" for p in obj.candidate_parent.all()]))
    view_parents.short_description = 'Parents'


@admin.register(CandidatePreviousSchool)
class PreviousSchoolAdmin(admin.ModelAdmin, ReadOnlyAdminMixin):
    list_display = ('candidate', 'school_name', 'date_history')

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

@admin.register(ParentInfo)
class ParentAdmin(admin.ModelAdmin, ReadOnlyAdminMixin):
    list_display = ('candidate', 'parent_surname', 'parent_name', 'contact_number', 'email_address')

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    
# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    extra = 0

    list_display = ['id', 'std_class']
    list_filter = ['id']

    fieldsets = [
        (None, {
            'fields': ['id', 'std_class']
        })
    ]

    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['id', 'std_class']
        }),
    ]

# @admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            # 'fields': ['id', 'category', 'subjects']
            'fields': ['idx', 'subjects']
        })
    ]

    add_fieldsets = [
        (
            {
                # 'fields': ['id', 'category', 'subjects']
                'fields': ['idx', 'subjects']
            }
        )
    ]

# @admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

# @admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Section)
class SectionAdmin(admin.ModelAdmin):
    model = Section
    extra = 0

    list_display = ['id', 'category']
    list_filter = ['id']

    fieldsets = [
        (None, {
            'fields': ['id', 'category']
        })
    ]
# @admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass

