from operator import add
from functools import reduce
from itertools import zip_longest


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


def create_tree_structure(PO):
    """
    Create tree structure (dict)
    :return: dictionary
    """
    tree_dict = {}
    prosecutor_offices = PO
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