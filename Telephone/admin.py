from django.contrib import admin
from Telephone.models import *


class PositionAdmin(admin.ModelAdmin):
    list_display = ('po_name', 'weight')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'position', 'work_telephone')
    list_display_links = ('surname', 'name', 'patronymic')
    list_editable = ('work_telephone',)
    search_fields = ('surname', 'name', 'patronymic', 'position', 'work_telephone')
    fields = (('name', 'surname', 'patronymic'), 'position', ('work_telephone', 'private_telephone'),
              'prosecutors_office', 'department', 'division')
    # raw_id_fields = ("position",)     если должностей будет очень много
    # list_per_page = 50
    # save_on_top = True        #для моделей с большим колвом данных


class DivisionAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class ProsecutorsOfficeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'counter_empl')
    fields = ('name', 'tel_cod', 'address', ('email_inside', 'email_outside'))

    def counter_empl(self, obj):
        """
        Подсчитывает количество работников в Прокуратуре
        :param obj: Передается сам обьект
        :return: Количество работников
        """
        return Employee.objects.filter(prosecutors_office__id=obj.id).count()
    counter_empl.short_description = "Количество работников"







admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(ProsecutorsOffice, ProsecutorsOfficeAdmin)




# class TeamForm(forms.ModelForm):
#     manager = forms.ModelChoiceField(queryset=User.objects.order_by('username'))
#
#     class Meta:
#         model = Team
#
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ('name', 'manager')
#     form = TeamForm
