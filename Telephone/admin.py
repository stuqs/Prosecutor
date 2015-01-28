from django.contrib import admin
# from Telephone.models import ProsecutorsOffice, Department, Division, Employee
from Telephone.models import *

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'position', 'work_telephone')
    search_fields = ('surname', 'name', 'patronymic', 'position', 'work_telephone')
    ordering = ('surname',)
    fields = (('name', 'surname', 'patronymic'), 'position', ('work_telephone', 'private_telephone'))


class ProsecutorsOfficeAdmin(admin.ModelAdmin):
    search_fields = ('surname', 'name', 'patronymic', 'position', 'work_telephone')
    filter_horizontal = ('department', 'division', 'employees')
    fieldsets = (
        (None, {
            'fields': ('name', 'department'),
        }),
        ('Дополнительные данные', {
            'classes': ('collapse',),
            'fields': ('tel_cod', 'address', ('email_inside', 'email_outside'))
        }),
    )



class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    filter_horizontal = ('division', 'employees')


class DivisionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    filter_horizontal = ('employees',)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('po_name', 'weigh')


admin.site.register(ProsecutorsOffice, ProsecutorsOfficeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)


# class TeamForm(forms.ModelForm):
#     manager = forms.ModelChoiceField(queryset=User.objects.order_by('username'))
#
#     class Meta:
#         model = Team
#
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ('name', 'manager')
#     form = TeamForm
