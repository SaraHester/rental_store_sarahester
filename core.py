# all logical functions go here
def make_inven_dict(inventory):
    '''[] -> {}'''
    number = 0
    dict_inventory = {}
    for line in inventory:
        number += 1
        item, price, quantity, value = line.strip().split(', ')
        dict_inventory[int(number)] = {'name': item, 'number': number, 'price': float(price), 'quantity': int(quantity), 'value': float(value)}
    return dict_inventory

def dict_inven_to_str(dict_inventory):
    '''dict{} -> str'''
    str_inventory = ''
    for item in dict_inventory:
        str_inventory += '\n' + str(dict_inventory[item]['name']) + ', ' +  str(dict_inventory[item]['price']) + ', ' +  str(dict_inventory[item]['quantity']) + ', ' +  str(dict_inventory[item]['value'])
    return str_inventory

def make_log_dict(log):
    '''[] -> {}'''
    dict_log = {}
    for line in log:
        i_d, name, time_out, time_in, total = line.strip().split(', ')
        dict_log[str(i_d)] = {'id': i_d, 'name': name, 'time checked out': time_out , 'time checked in': time_in, 'total': total}
    return dict_log

def make_log_str(dict_log):
    '''dict{} -> str'''
    str_log = ''
    for line in sorted(dict_log):
        str_log += '\n' + str(dict_log[line]['id']) + ', ' + str(dict_log[line]['name']) + ', ' + str(dict_log[line]['time checked out']) + ', ' + str(dict_log[line]['time checked in']) + ', ' + str(dict_log[line]['total'])
    return str_log

def log_line(dict_log, i_d, time_in, total):
    '''{}, str, str, float -> {}'''
    dict_log[i_d]['time checked in'] = time_in
    dict_log[i_d]['total'] = total
    return dict_log

def new_line(name, price, quantity, value):
    line = '\n' + str(name) + ', ' + str(price) + ', ' + str(quantity) + ', ' + str(value)
    return line

def rent_out(dict_inventory, number):
    ''''{}, int -> {}'''
    dict_inventory[number]['quantity'] -= 1
    return dict_inventory

def rent_in(dict_inventory, number):
    '''{}, int ->'''
    dict_inventory[number]['quantity'] += 1
    return dict_inventory

def rent_cost(dict_inventory, number, days):
    '''{}, int, int -> {}'''
    return dict_inventory[number]['price'] * int(days)

def deposit(dict_inventory, number):
    '''{}, int -> {}'''
    return dict_inventory[number]['value'] * .10

def sales_tax(cost):
    '''int-> int'''
    return cost * .07

def final_cost(dict_inventory, number, days):
    '''{}, int, int -> int'''
    cost = deposit(dict_inventory, number) + rent_cost(dict_inventory, number, days) 
    return  cost +  sales_tax(cost)

def check(dict_log, i_d_guess):
    '''{}, str -> str'''
    for line in dict_log:
        if str(i_d_guess) == str(line):
            return True
    else:
        return False

def check_quantity(dict_inventory):
    for item in dict_inventory:
        if dict_inventory[item]['quantity'] <= 1:
            return 0
    else:
        return 3