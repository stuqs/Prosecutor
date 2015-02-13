from Telephone.models import ProsecutorsOffice, Department, Division, Employee, Position
from django.contrib.auth.models import User


print(User.objects.create_superuser(username='admin', password='admin', email='A@A.nl'))

##################################################################

p1 = Position(po_name='Заступник начальника управління', weight=375)
p1.save()

p2 = Position(po_name='Начальник відділу', weight=350)
p2.save()

p3 = Position(po_name='Прокурор', weight=200)
p3.save()

p4 = Position(po_name='Прокурор області', weight=500)
p4.save()

p4 = Position(po_name='Заступник прокурора області', weight=450)
p4.save()

p5 = Position(po_name='Слідчий в ОВС', weight=150)
p5.save()

p6 = Position(po_name='Начальник управління', weight=400)
p6.save()

p7 = Position(po_name='Перший заступник прокурора області', weight=475)
p7.save()

p8 = Position(po_name='Старший прокурор', weight=250)
p8.save()

p9 = Position(po_name='Заступник начальника відділу', weight=325)
p9.save()

p10 = Position(po_name='Заступник начальника управління – начальник відділу', weight=390)
p10.save()

p11 = Position(po_name='Старший слідчий', weight=100)
p11.save()

p12 = Position(po_name='Старший прокурор відділу', weight=240)
p12.save()

p13 = Position(po_name='Прокурор відділу', weight=190)
p13.save()

p14 = Position(po_name='Головний спеціаліст - консультант', weight=90)
p14.save()

p15 = Position(po_name='Головний спеціаліст з питань мобілізаційної роботи', weight=85)
p15.save()

p16 = Position(po_name='Головний спеціаліст - психолог', weight=80)
p16.save()

p17 = Position(po_name='Провідний спеціаліст', weight=50)
p17.save()

p18 = Position(po_name='Спеціаліст 2 категорії', weight=40)
p18.save()

p19 = Position(po_name='Головний спеціаліст', weight=70)
p19.save()

p20 = Position(po_name='Завідувач господарства', weight=20)
p20.save()

p21 = Position(po_name='Завідувач складу', weight=15)
p21.save()

p21 = Position(po_name='Головний спеціаліст з питань захисту державних таємниць', weight=40)
p21.save()

p22 = Position(po_name='Начальник секретаріату', weight=90)
p22.save()

p23 = Position(po_name='Спеціаліст 1 категорії', weight=45)
p23.save()

p24 = Position(po_name='Завідувач копіювально-розмножувального бюро', weight=20)
p24.save()

p25 = Position(po_name='Архіваріус', weight=15)
p25.save()

p26 = Position(po_name='Начальник відділу – головний бухгалтер', weight=90)
p26.save()

p27 = Position(po_name='Заступник начальника відділу – заступник головного бухгалтера', weight=85)
p27.save()

p28 = Position(po_name='Прес-секретар', weight=30)
p28.save()

p29 = Position(po_name='Журналіст', weight=20)
p29.save()








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

