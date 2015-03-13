from operator import add
from functools import reduce
from itertools import zip_longest
import xlsxwriter


def roman2arabic(roman):
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if roman:
        return reduce(add, ((-d[x], d[x])[y is None or d[x] >= d[y]] for x, y in zip_longest(roman, roman[1:])))


def position_sort(emp_list):
    """
    :param emp_list: list of employees
    :return: sorted by position.weight list
    """
    return sorted(emp_list, key=lambda x=emp_list: (-x.position.weight, x.surname))


def adder(where, what, value):
    """
    Check if the dictionary has key(what), if not add to this key value(value)
    :param where: dictionary that checks
    :param what: key of dictionary
    :param value: value, that may be added
    :return: None
    """
    if what in where:
        pass
    else:
        where[what] = value


def create_employee_structure(employees):
    """
    Create structure (dict) from eployees list
    :param employees: list of employees
    :return: dictionary
    """
    employees_dict = {}
    for employee in position_sort(employees):
        if not employee.is_secretary:
            adder(employees_dict, employee.prosecutors_office, {'employees': [], 'departments': {}, 'divisions': {}})
            if employee.prosecutors_office and employee.department and employee.division:
                adder(employees_dict[employee.prosecutors_office]['departments'], employee.department, {})
                adder(employees_dict[employee.prosecutors_office]['departments'][employee.department], 'divisions', {})
                adder(employees_dict[employee.prosecutors_office]['departments'][employee.department]['divisions'], employee.division, [])
                employees_dict[employee.prosecutors_office]['departments'][employee.department]['divisions'][employee.division].append(employee)
            elif employee.prosecutors_office and employee.department:
                adder(employees_dict[employee.prosecutors_office]['departments'], employee.department, {})
                adder(employees_dict[employee.prosecutors_office]['departments'][employee.department], 'employees', [])
                employees_dict[employee.prosecutors_office]['departments'][employee.department]['employees'].append(employee)
            elif employee.prosecutors_office and employee.division:
                adder(employees_dict[employee.prosecutors_office]['divisions'], employee.division, [])
                employees_dict[employee.prosecutors_office]['divisions'][employee.division].append(employee)
            elif employee.prosecutors_office:
                employees_dict[employee.prosecutors_office]['employees'].append(employee)
    return employees_dict


def create_tree_structure(prosecutor_offices):
    """
    Create tree structure (dict)
    :return: dictionary
    """
    tree_dict = {}
    for prosecutor_office in prosecutor_offices:
        adder(tree_dict, prosecutor_office, {'departments': {}, 'divisions': []})
        for department in prosecutor_office.department_set.all():
            adder(tree_dict[prosecutor_office]['departments'], department, department.division_set.all())
        for division in prosecutor_office.division_set.all():
            if not division.department:
                tree_dict[prosecutor_office]['divisions'].append(division)
    return tree_dict


def regular_telephone(telephone_list):
    """
    Create nice view to telephone numbers
    """
    return_tel_list = []
    for telephone in telephone_list:
        if len(telephone) == 6:
            telephone = '{}-{}-{}'.format(telephone[0:2], telephone[2:4], telephone[4:6])
        elif len(telephone) == 7:
            telephone = '{}-{}-{}'.format(telephone[0:3], telephone[3:5], telephone[5:7])
        elif len(telephone) == 10:
            telephone = '{}-{}-{}-{}'.format(telephone[0:3], telephone[3:6], telephone[6:8], telephone[8:10])
        return_tel_list.append(telephone)
    return return_tel_list


def excel_out(employees_dict):
    """
    Create xlsx file with data from employees_dict
    """
    def add_header(worksheet, row, format):
        worksheet.merge_range(row, 0, row+1, 0, '№', cell_format=format)
        worksheet.merge_range(row, 1, row+1, 1, 'Фамилия имя отчество', cell_format=format)
        worksheet.merge_range(row, 2, row+1, 2, 'Должность', cell_format=format)
        worksheet.merge_range(row, 3, row, 4, 'Телефоны', cell_format=format)
        worksheet.write(row+1, 3, 'Служебный', format)
        worksheet.write(row+1, 4, 'Мобильный', format)
        return 2

    # Create workbook and worksheet
    workbook = xlsxwriter.Workbook(r'media/files/Tel_base.xlsx')
    worksheet = workbook.add_worksheet(name='Прокуратура')
    # Add format to workbook
    format_headers_po = workbook.add_format(           {'align':        'center',
                                                        'valign':       'vcenter',
                                                        'bold':         True,
                                                        'font_size':    14,
                                                        'font_name':    'Times New Roman',
                                                        'bg_color':     '#FFCA28',
                                                        'border':       2})
    format_headers_department = workbook.add_format(   {'align':        'center',
                                                        'valign':       'vcenter',
                                                        'bold':         True,
                                                        'font_size':    13,
                                                        'font_name':    'Times New Roman',
                                                        'bg_color':     '#FFD54F',
                                                        'border':       2})
    format_headers_division = workbook.add_format(     {'align':        'center',
                                                        'valign':       'vcenter',
                                                        'bold':         True,
                                                        'font_size':    12,
                                                        'font_name':    'Times New Roman',
                                                        'bg_color':     '#FFE082',
                                                        'border':       2})
    format_header = workbook.add_format(               {'align':        'center',
                                                        'valign':       'vcenter',
                                                        'bold':         True,
                                                        'font_size':    12,
                                                        'font_name':    'Times New Roman',
                                                        'bg_color':     '#FFF59D',
                                                        'border':       2})
    format_rows_bold = workbook.add_format(            {'align':        'left',
                                                        'valign':       'vcenter',
                                                        'text_wrap':    True,
                                                        'bold':         True,
                                                        'font_size':    12,
                                                        'font_name':    'Times New Roman',
                                                        'border':       2})
    format_rows = workbook.add_format(                 {'align':        'center',
                                                        'valign':       'vcenter',
                                                        'text_wrap':    True,
                                                        'font_size':    12,
                                                        'font_name':    'Times New Roman',
                                                        'border':       2})

    def add_employee(worksheet, row, employee, num):
        # Get number of row for employee
        if employee.work_telephone:
            work_telephone_list = regular_telephone(employee.work_telephone.split(';'))
        else:
            work_telephone_list = []
        if employee.private_telephone:
            private_telephone_list = regular_telephone(employee.private_telephone.split(';'))
        else:
            private_telephone_list = []
        rows_for_emp = max(len(work_telephone_list), len(private_telephone_list), 2)
        # Add name and position
        worksheet.merge_range(row, 0, row+rows_for_emp-1, 0, num, cell_format=format_rows)
        worksheet.merge_range(row, 1, row+rows_for_emp-1, 1, str(employee), cell_format=format_rows_bold)
        worksheet.merge_range(row, 2, row+rows_for_emp-1, 2, str(employee.position), cell_format=format_rows)
        # Add work telephone numbers
        for num, work_telephone in enumerate(work_telephone_list):
            if (len(work_telephone_list) < rows_for_emp) and ((num + 1) == len(work_telephone_list)):
                worksheet.merge_range(row+num, 3, row+rows_for_emp-1, 3, work_telephone, cell_format=format_rows)
            else:
                worksheet.write(row+num, 3, work_telephone, format_rows)
        if len(work_telephone_list) == 0:
            worksheet.merge_range(row, 3, row+rows_for_emp-1, 3, '', cell_format=format_rows)
        # Add private telephone numbers
        for num, private_telephone in enumerate(private_telephone_list):
            if (len(private_telephone_list) < rows_for_emp) and ((num + 1) == len(private_telephone_list)):
                worksheet.merge_range(row+num, 4, row+rows_for_emp-1, 4, private_telephone, cell_format=format_rows)
            else:
                worksheet.write(row+num, 4, private_telephone, format_rows)
            if (len(private_telephone_list) < rows_for_emp) and ((num - 1) == len(private_telephone_list)):
                worksheet.merge_range(row+num, 4, row+rows_for_emp-1, 4, '', cell_format=format_rows)
        if len(private_telephone_list) == 0:
            worksheet.merge_range(row, 4, row+rows_for_emp-1, 4, '', cell_format=format_rows)
        return rows_for_emp

    # Set width of columns and high of rows
    worksheet.set_default_row(40, False)
    worksheet.set_column(0, 0, 5)
    worksheet.set_column(1, 1, 25)
    worksheet.set_column(2, 2, 21)
    worksheet.set_column(3, 3, 21)
    worksheet.set_column(4, 4, 21)

    # Begin from row
    row = 0

    row += add_header(worksheet, row, format_header)

    for po in employees_dict:
        # Прокуратура
        # worksheet.write(row, 3, po.name, bold)
        worksheet.merge_range(row, 0, row, 4, data=po.name, cell_format=format_headers_po)
        row += 1
        # Атрибуты Прокуратуры

        # Работники Прокуратуры
        for num, employee in enumerate(employees_dict[po]['employees'], 1):
            row += add_employee(worksheet, row, employee, num)
            # worksheet.write(row, 1, str(employee), format_rows)
            # row += 1

        # Управление
        for department in employees_dict[po]['departments']:
            worksheet.merge_range(row, 0, row, 4, data=department.name, cell_format=format_headers_department)
            row += 1
            # Атрибуты Управления

            # Работники Управления
            for num, employee in enumerate(employees_dict[po]['departments'][department]['employees'], 1):
                row += add_employee(worksheet, row, employee, num)

            # Отдел Управления
            for division in employees_dict[po]['departments'][department]['divisions']:
                worksheet.merge_range(row, 0, row, 4, data=division.name, cell_format=format_headers_division)
                row += 1
                # Атрибуты Отдела

                # Работники Отдела
                for num, employee in enumerate(employees_dict[po]['departments'][department]['divisions'][division], 1):
                    row += add_employee(worksheet, row, employee, num)

        # Отдел Прокуратуры
        for division in employees_dict[po]['divisions']:
            worksheet.merge_range(row, 0, row, 4, data=division.name, cell_format=format_headers_division)
            row += 1
            # Атрибуты Отдела

            # Работники Отдела
            for num, employee in enumerate(employees_dict[po]['divisions'][division], 1):
                row += add_employee(worksheet, row, employee, num)

    try:
        workbook.close()
    except:
        print('Error during save')
        pass

    return r'media/files/Tel_base.xlsx'






"""
Ugly code
import re

s1 = "1111111111"
s2 = "1111111"
s3 = "111111"
PHONE_RE = re.compile(r'^(\d{3}|\d{2})()(\d{3}|\d{2})()(\d{2}|\d{2})()(\d{2}|)$')
MINUS_RE = re.compile(r'-$')

def format_phone_number(number):
  	temp = PHONE_RE.sub('\\1-\\3-\\5-\\7', number)
    return MINUS_RE.sub('', temp)

def main():
    for number in [s1, s2, s3]:
        print(format_phone_number(number))

if __name__ == '__main__':
    main()
"""

"""
filter for template
{% load your_file_name %}

{% for item in your_list|order_by:"field1,-field2,other_class__field_name"
1
2
3
4
5
6
7
8
from django.template import Library

register = Library()

@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)


"""