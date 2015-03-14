from django.db import models
from Telephone.tools import regular_telephone


class Position(models.Model):
    """
    Модель для должностей сотрудников, нужна что бы производить сортировку при выводе из БД
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
    surname = models.CharField(null=True, max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(blank=True, null=True, max_length=30, verbose_name='Отчество')
    position = models.ForeignKey(Position, null=True, verbose_name='Должность')
    work_telephone = models.CharField(blank=True, null=True, max_length=100, verbose_name='Служебный телефон',
                                      help_text='Номера разделяются символом ; - XXXX;YYYY')
    private_telephone = models.CharField(blank=True, null=True, max_length=100, verbose_name='Мобильный телефон',
                                         help_text='Номера разделяются символом ; - XXXX;YYYY')
    division = models.ForeignKey('Division', blank=True, null=True, verbose_name='Отдел')
    department = models.ForeignKey('Department', blank=True, null=True, verbose_name='Управление')
    prosecutors_office = models.ForeignKey('ProsecutorsOffice', blank=True, null=True, verbose_name='Прокуратура')
    secretary = models.ForeignKey('self', blank=True, null=True, verbose_name='Приемная')
    is_secretary = models.NullBooleanField(blank=True, null=True, verbose_name="Приемная")

    def tel_work_escape(self):
        """
        Returns tel. numbers with tegs if it is many (splitted by ;)
        """
        if self.work_telephone:
            return "<br>".join(regular_telephone(self.work_telephone.split(';')))
        else:
            return ''

    def tel_private_escape(self):
        """
        Returns tel. numbers with tegs if it is many (splitted by ;)
        """
        if self.private_telephone:
            return "<br>".join(regular_telephone(self.private_telephone.split(';')))
        else:
            return ''

    class Meta:
        order_with_respect_to = 'position'
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)


class Division(models.Model):
    """
    Модель для отделов
    """
    name = models.CharField(max_length=300, verbose_name='Отдел')
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Внешний e-mail')
    email_inside = models.EmailField(blank=True, null=True, verbose_name='Внутренний e-mail')
    address = models.CharField(blank=True, null=True, max_length=200, verbose_name='Адрес')
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
    address = models.CharField(blank=True, null=True, max_length=200, verbose_name='Адрес')
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Внешний e-mail')
    email_inside = models.EmailField(blank=True, null=True, verbose_name='Внутренний e-mail')

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
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Внешний e-mail')
    email_inside = models.EmailField(blank=True, null=True, verbose_name='Внутренний e-mail')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Прокуратура'
        verbose_name_plural = 'Прокуратуры'

    def __str__(self):
        return self.name