from django.contrib import admin
from Telephone.models import ProsecutorsOffice, Department, Division, Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'position', 'work_telephone')
    search_fields = ('surname', 'name', 'patronymic', 'position', 'work_telephone')
    ordering = ('surname',)


class ProsecutorsOfficeAdmin(admin.ModelAdmin):
    search_fields = ('surname', 'name', 'patronymic', 'position', 'work_telephone')
    filter_horizontal = ('department', 'division', 'employees')


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    filter_horizontal = ('division', 'employees')



class DivisionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    filter_horizontal = ('employees',)




admin.site.register(ProsecutorsOffice, ProsecutorsOfficeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Employee, EmployeeAdmin)