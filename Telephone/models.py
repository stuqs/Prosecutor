from django.db import models


class Employee(models.Model):
    """
    Модель для всех сотрудников
    """
    name = models.CharField(blank=True, max_length=30, verbose_name="Ім'я")
    surname = models.CharField(blank=True, max_length=30, verbose_name='Фамілія')
    patronymic = models.CharField(blank=True, max_length=30, verbose_name='По батькові')
    position = models.CharField(blank=True, max_length=100, verbose_name='Посада')
    # prosecutors_office = models.ForeignKey(ProsecutorsOffice, blank=True, null=True, verbose_name='Прокуратура', related_name='prosecutors_office')
    # department = models.ForeignKey(Department, blank=True, null=True, verbose_name='Управління', related_name='department')
    # division = models.ForeignKey(Division, blank=True, null=True, verbose_name='Відділ', related_name='division')
    work_telephone = models.CharField(blank=True, max_length=100, verbose_name='Службовий телефон', default='-',
                                      help_text='Номера разделяются символом ;')
    private_telephone = models.CharField(blank=True, max_length=100, verbose_name='Мобільний телефон', default='-',
                                         help_text='Номера разделяются символом ;')

    def __str__(self):
        return "{} {} {}".format(self.name, self.surname, self.patronymic)


class Division(models.Model):
    """
    Модель для отделов
    """
    name = models.CharField(max_length=300, verbose_name='Отдел')
    employees = models.ManyToManyField('Employee', blank=True, null=True, verbose_name='Працівники')

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    Модель для управлений
    """
    name = models.CharField(max_length=200, verbose_name='Управление')
    division = models.ManyToManyField(Division, blank=True, null=True, verbose_name='Отдел')
    employees = models.ManyToManyField('Employee', blank=True, null=True, verbose_name='Працівники',
                                       help_text='Работники без отдела, работающие в управлении <br>')

    def __str__(self):
        return self.name


class ProsecutorsOffice(models.Model):
    """
    Модель для прокуратур
    """
    name = models.CharField(max_length=300, verbose_name='Прокуратура')
    employees = models.ManyToManyField('Employee', blank=True, null=True, verbose_name='Працівники',
                                       help_text='Работники работающие напрямую в прокуратуре без управления и отдела<br>')
    department = models.ManyToManyField(Department, blank=True, null=True, verbose_name='Управління')
    address = models.CharField(blank=True, max_length=200, verbose_name='Адрес')
    email_inside = models.EmailField(blank=True, verbose_name='Внутрішній e-mail')
    email_outside = models.EmailField(blank=True, verbose_name='Зовнішній e-mail')
    tel_cod = models.CharField(blank=True, max_length=7, verbose_name='Телефонный код')

    def __str__(self):
        return self.name


