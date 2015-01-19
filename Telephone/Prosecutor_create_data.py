from Telephone.models import ProsecutorsOffice, Department, Division, Employee
from django.contrib.auth.models import User


print(User.objects.create_superuser(username='admin', password='admin', email='A@A.nl'))


d1 = Division(name='1) Відділ організації представництва на захист інтересів громадянина або держави')
d1.save()

d2 = Division(name='2) Відділ представництва інтересів громадян і держави в судах')
d2.save()

d3 = Division(name='3) Відділ представництва при виконанні судових рішень')
d3.save()

d4 = Division(name='4) Організаційно-методичний відділ')
d4.save()


D = Department(name='VIII. УПРАВЛІННЯ представництва, захисту інтересів громадян та держави в суді')
D.save()
D.division.add(d1, d2, d3, d4)


PO = ProsecutorsOffice(name='АПАРАТ', address='м.Одеса, вул. Пушкінська, 3', email_outside='Odeska.obl@od.gp.gov.ua',
                tel_cod='048')
PO.save()
PO.department.add(D)


e1 = Employee(name='Ярослав', surname='Заворотний', patronymic='Семенович', position='заступник начальника управління',
              prosecutors_office=PO, department=D, telephone='050-336-08-57')
e1.save()

e2 = Employee(name='Максим', surname='Ракович', patronymic='Миколайович', position='начальник відділу',
              prosecutors_office=PO, department=D, division=d1, telephone='067-484-46-84')
e2.save()

e3 = Employee(name='Сергій', surname='Бондарев', patronymic='Юрійович', position='прокурор',
              prosecutors_office=PO, department=D, division=d1, telephone='743-69-98')
e3.save()

e4 = Employee(name='Олексій', surname='Котелевський', patronymic='Іванович', position='начальник відділу',
              prosecutors_office=PO, department=D, division=d2, telephone='097-307-11-25')
e4.save()

e4 = Employee(name='Вадим', surname='Шивцов', patronymic='Михайлович', position='начальник відділу',
              prosecutors_office=PO, department=D, division=d2, telephone='096-288-83-90')
e4.save()
