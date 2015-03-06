from django.contrib import admin
from Telephone.models import *


class PositionAdmin(admin.ModelAdmin):
    list_display = ('po_name', 'weight')

# class ProsecutorsOfficeInline(admin.TabularInline):
#     model = Employee
#     extra = 2

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'position', 'work_telephone')
    ordering = ['position']
    list_display_links = ('surname', 'name', 'patronymic')
    list_editable = ('work_telephone',)
    search_fields = ('surname', 'name', 'patronymic', 'position', 'work_telephone')
    fields = (('name', 'surname', 'patronymic'), 'position', ('work_telephone', 'private_telephone'),
              'prosecutors_office', 'department', 'division')
    raw_id_fields = ('position',)#     если должностей будет очень много(поле поиска а не селект)
    # list_per_page = 50
    # save_on_top = True        #для моделей с большим колвом данных (добавляет поле сохранения сверху)

    def save_model(self, request, obj, form, change):
        """
        Function for editing object before save, set the right division-department-po tree structure, edit telephones
        """
        if obj.work_telephone:
            obj.work_telephone = obj.work_telephone.replace("-", "")
            obj.work_telephone = obj.work_telephone.replace(" ", "")
        if obj.private_telephone:
            obj.private_telephone = obj.private_telephone.replace("-", "")
            obj.private_telephone = obj.private_telephone.replace(" ", "")
        if obj.division:
            obj.department = obj.division.department
            obj.prosecutors_office = obj.division.prosecutors_office
        elif obj.department:
            obj.prosecutors_office = obj.department.prosecutors_office
        obj.save()


class DivisionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = ('name', 'department', 'prosecutors_office', 'address', ('email_inside', 'email_outside'))
    list_display = ('name', 'counter_empl')


    def counter_empl(self, obj):
        """
        Count for eployees in Division
        :param obj: Division object
        :return: Number of employees
        """
        return Employee.objects.filter(division__id=obj.id).count()
    counter_empl.short_description = "Количество работников"

    def save_model(self, request, obj, form, change):
        """
        Function for editing object before save, set the right department-po tree structure
        """
        if obj.department:
            obj.prosecutors_office = obj.department.prosecutors_office
        obj.save()


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = ('name', 'prosecutors_office', 'address', ('email_inside', 'email_outside'))
    list_display = ('name', 'counter_empl')

    def counter_empl(self, obj):
        """
        Count for eployees in Department
        :param obj: Department object
        :return: Number of employees
        """
        return Employee.objects.filter(department__id=obj.id).count()
    counter_empl.short_description = "Количество работников"

class ProsecutorsOfficeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'counter_empl')
    fields = ('name', 'tel_cod', 'address', ('email_inside', 'email_outside'))
    # inlines = (ProsecutorsOfficeInline, )

    def counter_empl(self, obj):
        """
        Count for eployees in PO
        :param obj: PO object
        :return: Number of employees
        """
        return Employee.objects.filter(prosecutors_office__id=obj.id).count()
    counter_empl.short_description = "Количество работников"


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(ProsecutorsOffice, ProsecutorsOfficeAdmin)