from django.db import models

#
# class Employee(models.Model):
#     """
#     Модель для всех сотрудников
#     """
#     name = models.CharField(blank=True, null=True, max_length=30, verbose_name="Ім'я")
#     surname = models.CharField(blank=True, null=True, max_length=30, verbose_name='Фамілія')
#     patronymic = models.CharField(blank=True, null=True, max_length=30, verbose_name='По батькові')
#     position = models.CharField(blank=True, null=True, max_length=100, verbose_name='Посада')
#     work_telephone = models.CharField(blank=True, null=True, max_length=100, verbose_name='Службовий телефон', default='-',
#                                       help_text='Номера разделяются символом ;')
#     private_telephone = models.CharField(blank=True, null=True, max_length=100, verbose_name='Мобільний телефон', default='-',
#                                          help_text='Номера разделяются символом ;')
#
#     def __str__(self):
#         return "{} {} {}".format(self.name, self.surname, self.patronymic)
#
#     class Meta:
#         # order_with_respect_to = 'position'
#         pass
#
#
#
# class Division(models.Model):
#     """
#     Модель для отделов
#     """
#     name = models.CharField(max_length=300, verbose_name='Відділ')
#     employees = models.ManyToManyField('Employee', blank=True, null=True, verbose_name='Працівники')
#     email_outside = models.EmailField(blank=True, null=True, verbose_name='Зовнішній e-mail')
#
#     def __str__(self):
#         return self.name
#
#
# class Department(models.Model):
#     """
#     Модель для управлений
#     """
#     name = models.CharField(max_length=200, verbose_name='Управління')
#     division = models.ManyToManyField(Division, blank=True, null=True, verbose_name='Відділ')
#     employees = models.ManyToManyField('Employee', blank=True, null=True, verbose_name='Працівники',
#                                        help_text='Работники без отдела, работающие в управлении <br>')
#     email_outside = models.EmailField(blank=True, null=True, verbose_name='Зовнішній e-mail')
#
#     def __str__(self):
#         return self.name
#
#
# class ProsecutorsOffice(models.Model):
#     """
#     Модель для прокуратур
#     """
#     name = models.CharField(max_length=300, verbose_name='Прокуратура')
#     department = models.ManyToManyField(Department, blank=True, null=True, verbose_name='Управління')
#     division = models.ManyToManyField(Division, blank=True, null=True, verbose_name='Відділ')
#     employees = models.ManyToManyField('Employee', blank=True, null=True, verbose_name='Працівники',
#                                        help_text='Работники работающие напрямую в прокуратуре без управления и отдела<br>')
#     tel_cod = models.CharField(blank=True, null=True, max_length=7, verbose_name='Телефонный код')
#     address = models.CharField(blank=True, null=True, max_length=200, verbose_name='Адрес')
#     email_inside = models.EmailField(blank=True, null=True, verbose_name='Внутрішній e-mail')
#     email_outside = models.EmailField(blank=True, null=True, verbose_name='Зовнішній e-mail')
#
#     def __str__(self):
#         return self.name


from django.db import models


class Position(models.Model):
    """
    Модель для всех должности сотрудников, нужна что бы производить сортировку при выводе из БД
    """
    position = models.CharField(max_length=100, verbose_name='Посада')

    def __str__(self):
        return self.position

class Employee(models.Model):
    """
    Модель для всех сотрудников
    """
    name = models.CharField(blank=True, null=True, max_length=30, verbose_name="Ім'я")
    surname = models.CharField(blank=True, null=True, max_length=30, verbose_name='Фамілія')
    patronymic = models.CharField(blank=True, null=True, max_length=30, verbose_name='По батькові')
    position = models.ForeignKey(Position, blank=True, null=True, verbose_name='Посада')
    work_telephone = models.CharField(blank=True, null=True, max_length=100, verbose_name='Службовий телефон',
                                      default='-', help_text='Номера разделяются символом ;')
    private_telephone = models.CharField(blank=True, null=True, max_length=100, verbose_name='Мобільний телефон',
                                         default='-', help_text='Номера разделяются символом ;')

    def __str__(self):
        return "{} {} {}".format(self.name, self.surname, self.patronymic)

    class Meta:
        order_with_respect_to = 'position'


class Division(models.Model):
    """
    Модель для отделов
    """
    name = models.CharField(max_length=300, verbose_name='Відділ')
    employees = models.ManyToManyField('Employee', blank=True, null=True, verbose_name='Працівники')
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Зовнішній e-mail')

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    Модель для управлений
    """
    name = models.CharField(max_length=200, verbose_name='Управління')
    division = models.ManyToManyField(Division, blank=True, null=True, verbose_name='Відділ')
    employees = models.ManyToManyField('Employee', blank=True, null=True, verbose_name='Працівники',
                                       help_text='Работники без отдела, работающие в управлении <br>')
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Зовнішній e-mail')

    def __str__(self):
        return self.name


class ProsecutorsOffice(models.Model):
    """
    Модель для прокуратур
    """
    name = models.CharField(max_length=300, verbose_name='Прокуратура')
    department = models.ManyToManyField(Department, blank=True, null=True, verbose_name='Управління')
    division = models.ManyToManyField(Division, blank=True, null=True, verbose_name='Відділ')
    employees = models.ManyToManyField('Employee', blank=True, null=True, verbose_name='Працівники',
                                       help_text='Работники работающие напрямую в прокуратуре без управления и отдела<br>')
    tel_cod = models.CharField(blank=True, null=True, max_length=7, verbose_name='Телефонный код')
    address = models.CharField(blank=True, null=True, max_length=200, verbose_name='Адрес')
    email_inside = models.EmailField(blank=True, null=True, verbose_name='Внутрішній e-mail')
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Зовнішній e-mail')

    def __str__(self):
        return self.name
