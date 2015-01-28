from django.db import models


class Position(models.Model):
    """
    Модель для всех должности сотрудников, нужна что бы производить сортировку при выводе из БД
    """
    po_name = models.CharField(max_length=100, verbose_name='Посада')
    weigh = models.PositiveSmallIntegerField(verbose_name='Вес для сортировки', default=1)

    class Meta:
        ordering = ('-weigh',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.po_name


class Employee(models.Model):
    """
    Модель для всех сотрудников
    """
    name = models.CharField(blank=True, null=True, max_length=30, verbose_name="Ім'я")
    surname = models.CharField(blank=True, null=True, max_length=30, verbose_name='Фамілія')
    patronymic = models.CharField(blank=True, null=True, max_length=30, verbose_name='По батькові')
    position = models.ForeignKey(Position, blank=True, null=True, verbose_name='Посада')
    work_telephone = models.CharField(blank=True, null=True, max_length=100, verbose_name='Службовий телефон',
                                      default='-', help_text='Номера разделяются символом ; - XXXX;YYYY')
    private_telephone = models.CharField(blank=True, null=True, max_length=100, verbose_name='Мобільний телефон',
                                         default='-', help_text='Номера разделяются символом ; - XXXX;YYYY')

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
    name = models.CharField(max_length=300, verbose_name='Відділ')
    employees = models.ManyToManyField('Employee', blank=True, verbose_name='Працівники')
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Зовнішній e-mail')

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
    name = models.CharField(max_length=200, verbose_name='Управління')
    division = models.ManyToManyField(Division, blank=True, verbose_name='Відділ')
    employees = models.ManyToManyField('Employee', blank=True, verbose_name='Працівники',
                                       help_text='Работники без отдела, работающие в управлении <br>')
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Зовнішній e-mail')

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
    department = models.ManyToManyField(Department, blank=True, verbose_name='Управління')
    division = models.ManyToManyField(Division, blank=True, verbose_name='Відділ')
    employees = models.ManyToManyField('Employee', blank=True, verbose_name='Працівники',
                                       help_text='Работники работающие напрямую в прокуратуре без управления и отдела<br>')
    tel_cod = models.CharField(blank=True, null=True, max_length=7, verbose_name='Телефонный код')
    address = models.CharField(blank=True, null=True, max_length=200, verbose_name='Адрес')
    email_inside = models.EmailField(blank=True, null=True, verbose_name='Внутрішній e-mail')
    email_outside = models.EmailField(blank=True, null=True, verbose_name='Зовнішній e-mail')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Прокуратура'
        verbose_name_plural = 'Прокуратуры'

    def __str__(self):
        return self.name




