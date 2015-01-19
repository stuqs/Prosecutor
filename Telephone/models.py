from django.db import models


class Division(models.Model):
    """
    Модель для отделов
    """
    name = models.CharField(max_length=300, verbose_name='Отдел')

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    Модель для управлений
    """
    name = models.CharField(max_length=200, verbose_name='Управление')
    division = models.ManyToManyField(Division, blank=True, null=True, verbose_name='Отдел')

    def __str__(self):
        return self.name


class ProsecutorsOffice(models.Model):
    """
    Модель для прокуратур
    """
    name = models.CharField(max_length=300, verbose_name='Прокуратура')
    department = models.ManyToManyField(Department, blank=True, null=True, verbose_name='Управление')
    address = models.CharField(blank=True, max_length=200, verbose_name='Адрес')
    email_inside = models.EmailField(blank=True, verbose_name='Внутренний e-mail')
    email_outside = models.EmailField(blank=True, verbose_name='Внешний e-mail')
    tel_cod = models.CharField(blank=True, max_length=7, verbose_name='Теллефонный код')

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Модель для всех сотрудников
    """
    name = models.CharField(blank=True, max_length=30, verbose_name='Имя')
    surname = models.CharField(blank=True, max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(blank=True, max_length=30, verbose_name='Отчество')
    position = models.CharField(blank=True, max_length=100, verbose_name='Посада')
    prosecutors_office = models.ForeignKey(ProsecutorsOffice, blank=True, null=True, verbose_name='Прокуратура')
    department = models.ForeignKey(Department, blank=True, null=True, verbose_name='Управління')
    division = models.ForeignKey(Division, blank=True, null=True, verbose_name='Відділ')
    work_telephone = models.CharField(blank=True, max_length=100, verbose_name='Службовий телефон')
    private_telephone = models.CharField(blank=True, max_length=100, verbose_name='Мобільний телефон')

    def __str__(self):
        return "{} {} {}".format(self.name, self.surname, self.patronymic)