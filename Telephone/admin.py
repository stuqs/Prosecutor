from django.contrib import admin
# from Telephone.models import ProsecutorsOffice, Department, Division, Employee
from Telephone.models import *

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'position', 'work_telephone', 'weight')
    list_display_links = ('surname', 'name', 'patronymic')
    list_editable = ('position', 'work_telephone')
    search_fields = ('surname', 'name', 'patronymic', 'position', 'work_telephone')
    ordering = ('surname',)
    fields = (('name', 'surname', 'patronymic'), 'position', ('work_telephone', 'private_telephone'))
    # raw_id_fields = ("position",)     если должностей будет очень много
    # list_per_page = 50
    # save_on_top = True        для моделей с большим колвом данных

    def weight(self, obj):
        return obj.position.weight

class ProsecutorsOfficeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    filter_horizontal = ('department', 'division', 'employees')
    list_display = ('name', 'counter_empl')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'department', 'division', 'employees'),
        }),
        ('Дополнительные данные', {
            'classes': ('collapse',),
            'fields': ('tel_cod', 'address', ('email_inside', 'email_outside'))
        }),
    )

    def counter_empl(self, obj):
        """
        Подсчитывает количество работников
        :param obj: Передается сам обьект
        :return: Количество работников
        """
        return obj.employees.count()
    counter_empl.short_description = "Тестовая функция из admin"


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    filter_horizontal = ('division', 'employees')
    ordering = ('name',)


class DivisionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    filter_horizontal = ('employees',)
    ordering = ('name',)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('po_name', 'weight')
    ordering = ('-weight',)


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
