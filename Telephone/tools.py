from operator import add
from functools import reduce
from itertools import zip_longest
import xlsxwriter
import os


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
        if len(telephone) == 4:
            telephone = '{}{}{}'.format('<b>', telephone, '</b>')
        elif len(telephone) == 5:
            telephone = '{}-{}-{}'.format(telephone[0], telephone[1:3], telephone[3:5])
        elif len(telephone) == 6:
            if telephone[0] == '8':
                telephone = '{}({})-{}{}'.format('<b>', telephone[0:3], telephone[3:6], '</b>')
            else:
                telephone = '{}-{}-{}'.format(telephone[0:2], telephone[2:4], telephone[4:6])
        elif len(telephone) == 7:
            telephone = '{}-{}-{}'.format(telephone[0:3], telephone[3:5], telephone[5:7])
        elif len(telephone) == 10:
            telephone = '{}-{}-{}-{}'.format(telephone[0:3], telephone[3:6], telephone[6:8], telephone[8:10])
        return_tel_list.append(telephone)
    return_tel_list.sort(key=lambda x: len(x), reverse=True)
    return return_tel_list


####################################################################
                        # Excel section
####################################################################
def create_file(employee_list, path):
    """
    Create excel file from employee_list
    """
    employees_dict = create_employee_structure(employee_list)
    return excel_out(employees_dict, path)


def open_file(path):
    try:
        fsock = open(path, 'rb')
    except FileNotFoundError:
        return False
    return fsock


def add_header(worksheet, row, header_format):
    """
    Add header to worksheet
    """
    worksheet.write(row, 0,  '№', header_format)
    worksheet.write(row, 1,  'Фамилия имя отчество', header_format)
    worksheet.write(row, 2,  'Должность', header_format)
    worksheet.write(row, 3, 'Служебный тел.', header_format)
    worksheet.write(row, 4, 'Мобильный тел.', header_format)
    return row+1


def add_attribute(temp_node, worksheet, row, attr_format):
    """
    Add attributes for po/department/division to worksheet
    """
    if temp_node.address or getattr(temp_node, 'tel_cod', None) or temp_node.email_inside or temp_node.email_outside:
        if temp_node.address:
            worksheet.merge_range(row, 0, row, 4, 'Адресс: ' + str(temp_node.address), cell_format=attr_format)
            worksheet.set_row(row, 20)
            row += 1
        if getattr(temp_node, 'tel_cod', None):
            worksheet.merge_range(row, 0, row, 4, 'Теллефонный код: ' + str(temp_node.tel_cod), cell_format=attr_format)
            worksheet.set_row(row, 20)
            row += 1
        if temp_node.email_inside or temp_node.email_outside:
            worksheet.merge_range(row, 0, row, 4, 'Электронный адресс: ', cell_format=attr_format)
            worksheet.set_row(row, 20)
            row += 1
            if temp_node.email_inside:
                worksheet.merge_range(row, 0, row, 4, 'Внутренний: ' + str(temp_node.email_inside), cell_format=attr_format)
                worksheet.set_row(row, 20)
                row += 1
            if temp_node.email_outside:
                worksheet.merge_range(row, 0, row, 4, 'Внешний: ' + str(temp_node.email_outside), cell_format=attr_format)
                worksheet.set_row(row, 20)
                row += 1
    return row

def telephone_strip(telephone_list):
    """
    Create  view to telephone numbers in Excel
    """
    tel_list = []
    for telephone in telephone_list:
        if len(telephone) == 4:
            pass
            # MAKE BOLD STYLE
        elif len(telephone) == 5:
            telephone = '{}-{}-{}'.format(telephone[0], telephone[1:3], telephone[3:5])
        elif len(telephone) == 6:
            if telephone[0] == '8':
                telephone = '({})-{}'.format(telephone[0:3], telephone[3:6])
                 # MAKE BOLD STYLE
            else:
                telephone = '{}-{}-{}'.format(telephone[0:2], telephone[2:4], telephone[4:6])
        elif len(telephone) == 7:
            telephone = '{}-{}-{}'.format(telephone[0:3], telephone[3:5], telephone[5:7])
        elif len(telephone) == 10:
            telephone = '{}-{}-{}-{}'.format(telephone[0:3], telephone[3:6], telephone[6:8], telephone[8:10])
        tel_list.append(telephone)
    tel_list.sort(key=lambda x: len(x), reverse=True)
    return tel_list

def add_employee(worksheet, row, employee, num_in_list, employee_format, employee_format_b):
    """
    Add employee to worksheet
    """
    # Get number of row for employee
    if employee.work_telephone:
        work_telephone_list = telephone_strip(employee.work_telephone.split(';'))
    else:
        work_telephone_list = []
    if employee.private_telephone:
        private_telephone_list = telephone_strip(employee.private_telephone.split(';'))
    else:
        private_telephone_list = []
    # REMAKE THIS FUNTION to styles
    # rows_for_emp = max(len(work_telephone_list), len(private_telephone_list), 2)
        # Count for max tel numbers
    # Add name and position
    worksheet.write(row, 0, num_in_list, employee_format)
    if employee.is_secretary:
        worksheet.write(row, 1, '', employee_format_b)
    else:
        worksheet.write(row, 1, str(employee), employee_format_b)
    worksheet.write(row, 2, str(employee.position), employee_format)
    # Add telephones numbers
    work_telephone_str = '\n'.join(work_telephone_list)
    private_telephone_str = '\n'.join(private_telephone_list)
    worksheet.write(row, 3, work_telephone_str, employee_format)
    worksheet.write(row, 4, private_telephone_str, employee_format)
    # If secretary exist
    if employee.secretary:
        row += 1
        row = add_employee(worksheet, row, employee.secretary, '', employee_format, employee_format_b)
    else:
        row += 1
    return row


def excel_out(employees_dict, path):
    """
    Create xlsx file with data from employees_dict
    """
    # Create workbook and worksheet
    try:
        workbook = xlsxwriter.Workbook(path)
    except:
        return False
    worksheet = workbook.add_worksheet(name='Прокуратура')
    # Add format to workbook
    format_headers_po = workbook.add_format(           {'align':        'center',
                                                        'valign':       'vcenter',
                                                        'bold':         True,
                                                        'font_size':    14,
                                                        'font_name':    'Times New Roman',
                                                        'bg_color':     '#FFCA28',
                                                        'border':       2})
    format_headers_po.set_text_wrap()
    format_headers_department = workbook.add_format(   {'align':        'center',
                                                        'valign':       'vcenter',
                                                        'bold':         True,
                                                        'font_size':    13,
                                                        'font_name':    'Times New Roman',
                                                        'bg_color':     '#FFD54F',
                                                        'border':       2})
    format_headers_department.set_text_wrap()
    format_headers_division = workbook.add_format(     {'align':        'center',
                                                        'valign':       'vcenter',
                                                        'bold':         True,
                                                        'font_size':    12,
                                                        'font_name':    'Times New Roman',
                                                        'bg_color':     '#FFE082',
                                                        'border':       2})
    format_headers_division.set_text_wrap()
    format_header = workbook.add_format(               {'align':        'center',
                                                        'valign':       'vcenter',
                                                        'bold':         True,
                                                        'font_size':    12,
                                                        'font_name':    'Times New Roman',
                                                        'bg_color':     '#FFF59D',
                                                        'border':       2})
    format_header.set_text_wrap()
    employee_format_b = workbook.add_format(           {'align':        'left',
                                                        'valign':       'vcenter',
                                                        'text_wrap':    True,
                                                        'bold':         True,
                                                        'font_size':    12,
                                                        'font_name':    'Times New Roman',
                                                        'border':       2})
    employee_format_b.set_text_wrap()
    employee_format = workbook.add_format(             {'align':        'center',
                                                        'valign':       'vcenter',
                                                        'text_wrap':    True,
                                                        'font_size':    12,
                                                        'font_name':    'Times New Roman',
                                                        'border':       2})
    employee_format.set_text_wrap()
    format_attribute = workbook.add_format(            {'align':        'center',
                                                        'valign':       'vcenter',
                                                        'text_wrap':    True,
                                                        'font_size':    10,
                                                        'font_name':    'Times New Roman',
                                                        'border':       1})
    format_attribute.set_text_wrap()

    # Set width of columns and height of rows
    worksheet.set_default_row(60, False)
    worksheet.set_column(0, 0, 5)
    worksheet.set_column(1, 1, 25)
    worksheet.set_column(2, 2, 21)
    worksheet.set_column(3, 3, 21)
    worksheet.set_column(4, 4, 21)

    # Begin from row
    row = 0

    # Parser for employees dictionary
    for po in employees_dict:
        # Прокуратура
        worksheet.merge_range(row, 0, row, 4, data=po.name, cell_format=format_headers_po)
        row += 1
        # Атрибуты Прокуратуры
        row = add_attribute(po, worksheet, row, format_attribute)
        # Header
        row = add_header(worksheet, row, format_header)
        # Работники Прокуратуры
        if 'employees' in employees_dict[po] and employees_dict[po]['employees']:
            for num, employee in enumerate(employees_dict[po]['employees'], 1):
                row = add_employee(worksheet, row, employee, num, employee_format, employee_format_b)

        # Управление
        if 'departments' in employees_dict[po] and employees_dict[po]['departments']:
            for department in employees_dict[po]['departments']:
                worksheet.merge_range(row, 0, row, 4, data=department.name, cell_format=format_headers_department)
                row += 1
                # Атрибуты Управления
                row = add_attribute(department, worksheet, row, format_attribute)
                # Работники Управления
                if 'employees' in employees_dict[po]['departments'][department]:
                    for num, employee in enumerate(employees_dict[po]['departments'][department]['employees'], 1):
                        row = add_employee(worksheet, row, employee, num, employee_format, employee_format_b)
                # Отдел Управления
                if 'divisions' in employees_dict[po]['departments'][department]:
                    for division in employees_dict[po]['departments'][department]['divisions']:
                        worksheet.merge_range(row, 0, row, 4, data=division.name, cell_format=format_headers_division)
                        row += 1
                        # Атрибуты Отдела
                        row = add_attribute(division, worksheet, row, format_attribute)
                        # Работники Отдела
                        for num, employee in enumerate(employees_dict[po]['departments'][department]['divisions'][division], 1):
                            row = add_employee(worksheet, row, employee, num, employee_format, employee_format_b)

    try:
        workbook.close()
    except:
        return False
    return True