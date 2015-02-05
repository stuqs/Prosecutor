from Telephone.models import ProsecutorsOffice, Department, Division, Employee, Position
from django.contrib.auth.models import User


print(User.objects.create_superuser(username='admin', password='admin', email='A@A.nl'))

##################################################################

p1 = Position(po_name='заступник начальника управління', weight=250)
p1.save()

p2 = Position(po_name='начальник відділу', weight=200)
p2.save()

p3 = Position(po_name='прокурор', weight=100)
p3.save()

p4 = Position(po_name='Прокурор области', weight=500)
p4.save()

p4 = Position(po_name='Заступник Прокурор области', weight=400)
p4.save()

p5 = Position(po_name='Техныч працывник', weight=50)
p5.save()

p6 = Position(po_name='начальник управлыння', weight=300)
p6.save()

##################################################################

e1 = Employee(name='Ярослав', surname='Заворотний', patronymic='Семенович', position=p1,
              private_telephone='050-336-08-57')
e1.save()

e2 = Employee(name='Максим', surname='Ракович', patronymic='Миколайович', position=p2,
              work_telephone='1500;731-98-62',
              private_telephone='067-484-46-84')
e2.save()

e3 = Employee(name='Сергій', surname='Бондарев', patronymic='Юрійович', position=p3,
              work_telephone='1514;731-99-63',
              private_telephone='743-69-98')
e3.save()

e4 = Employee(name='Олексій', surname='Котелевський', patronymic='Іванович', position=p2,
              work_telephone='1105;731-98-67',
              private_telephone='097-307-11-25')
e4.save()

e5 = Employee(name='Вадим', surname='Шивцов', patronymic='Михайлович', position=p3,
              private_telephone='096-288-83-90')
e5.save()

##################################################################

d1 = Division(name='1) Відділ організації представництва на захист інтересів громадянина або держави')
d1.save()
d1.employees.add(e2, e3)

d2 = Division(name='2) Відділ представництва інтересів громадян і держави в судах')
d2.save()
d2.employees.add(e4, e5)

d3 = Division(name='3) Відділ представництва при виконанні судових рішень')
d3.save()

d4 = Division(name='4) Організаційно-методичний відділ')
d4.save()

##################################################################

D = Department(name='VIII. УПРАВЛІННЯ представництва, захисту інтересів громадян та держави в суді')
D.save()
D.employees.add(e1)

##################################################################

PO = ProsecutorsOffice(name='АПАРАТ', address='м.Одеса, вул. Пушкінська, 3', email_outside='Odeska.obl@od.gp.gov.ua',
                       tel_cod='048')
PO.save()
PO.department.add(D)

