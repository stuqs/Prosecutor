from django.db import models


class Position(models.Model):
    """
    Модель для всех должности сотрудников, нужна что бы производить сортировку при выводе из БД
    """
    po_name = models.CharField(max_length=100, verbose_name='Должность')
    weight = models.PositiveSmallIntegerField(verbose_name='Вес для сортировки', default=1)

    class Meta:
        ordering = ('-weight',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.po_name


class Employee(models.Model):
    """
    Модель для всех сотрудников
    """
    name = models.CharField(blank=True, null=True, max_length=30, verbose_name="Имя")
    surname = models.CharField(blank=True, null=True, max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(blank=True, null=True, max_length=30, verbose_name='Отчество')
    position = models.ForeignKey(Position, blank=True, null=True, verbose_name='Должность')
    work_telephone = models.CharField(blank=True, null=True, max_length=100, verbose_name='Служебный телефон',
                                      default='-', help_text='Номера разделяются символом ; - XXXX;YYYY')
    private_telephone = models.CharField(blank=True, null=True, max_length=100, verbose_name='Мобильный телефон',
                                         default='-', help_text='Номера разделяются символом ; - XXXX;YYYY')
    division = models.ForeignKey('Division', blank=True, null=True, verbose_name='Отдел')
    department = models.ForeignKey('Department', blank=True, null=True, verbose_name='Управление')
    prosecutors_office = models.ForeignKey('ProsecutorsOffice', blank=True, null=True, verbose_name='Прокуратура')

    def tel_work_escape(self):
        return "<br>".join(self.work_telephone.replace(" ", "").split(';'))

    def tel_private_escape(self):
        return "<br>".join(self.private_telephone.replace(" ", "").split(';'))

    class Meta:
        order_with_respect_to = 'position'
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return "{} {} {}".format(self.name, self.surname, self.patronymic)


class Division(models.Model):
    """
    Модель для отделов
    """
    name = models.CharField(max_length=300, verbose_name='Отдел')
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Внешний e-mail')
    department = models.ForeignKey('Department', blank=True, null=True, verbose_name='Управление')
    prosecutors_office = models.ForeignKey('ProsecutorsOffice', blank=True, null=True, verbose_name='Прокуратура')


    class Meta:
        ordering = ('name',)
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    Модель для управлений
    """
    name = models.CharField(max_length=200, verbose_name='Управление')
    prosecutors_office = models.ForeignKey('ProsecutorsOffice', blank=True, null=True, verbose_name='Прокуратура')
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Внешний e-mail')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Управление'
        verbose_name_plural = 'Управления'

    def __str__(self):
        return self.name


class ProsecutorsOffice(models.Model):
    """
    Модель для прокуратур
    """
    name = models.CharField(max_length=300, verbose_name='Прокуратура')
    tel_cod = models.CharField(blank=True, null=True, max_length=7, verbose_name='Телефонный код')
    address = models.CharField(blank=True, null=True, max_length=200, verbose_name='Адрес')
    email_inside = models.EmailField(blank=True, null=True, verbose_name='Внутренний e-mail')
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Внешний e-mail')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Прокуратура'
        verbose_name_plural = 'Прокуратуры'

    def __str__(self):
        return self.name