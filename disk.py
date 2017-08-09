#Opening and closing files goes here
import core


def make_inven_dict(inventory):
    '''[] -> {}'''
    number = 0
    dict_inventory = {}
    for line in inventory:
        number += 1
        item, price, quantity, value = line.strip().split(', ')
        dict_inventory[int(number)] = {
            'name': item,
            'number': number,
            'price': float(price),
            'quantity': int(quantity),
            'value': float(value)
        }
    return dict_inventory


def dict_inven_to_str(dict_inventory):
    '''dict{} -> str'''
    str_inventory = ''
    for item in dict_inventory:
        str_inventory += '\n' + str(dict_inventory[item]['name']) + ', ' + str(
            dict_inventory[item]['price']) + ', ' + str(
                dict_inventory[item]['quantity']) + ', ' + str(
                    dict_inventory[item]['value'])
    return str_inventory


def make_log_dict(log):
    '''[] -> {}'''
    dict_log = {}
    for line in log:
        i_d, name, time, total, rent_status = line.strip().split(', ')
        dict_log[str(i_d)] = {
            'id': i_d,
            'name': name,
            'time': time,
            'total': total,
            'rent status': rent_status
        }
    return dict_log


def make_log_str(dict_log):
    '''dict{} -> str'''
    str_log = ''
    for line in sorted(dict_log):
        str_log += '\n' + str(dict_log[line]['id']) + ', ' + str(
            dict_log[line]['name']) + ', ' + str(
                dict_log[line]['time']) + ', ' + str(
                    dict_log[line]['total']) + ', ' + str(
                        cict_log[line]['rent status'])
    return str_log


def open_inventory():
    with open('inventory.txt', 'r') as file:
        file.readline()
        inventory = file.readlines()
    return make_inven_dict(inventory)


def append_inventory(inventory):
    with open('inventory.txt', 'a') as file:
        file.write(inventory)


def rewrite_inventory(inventory):
    with open('inventory.txt', 'w') as file:
        file.write(dict_inven_to_str(inventory))


def open_log():
    with open('history.txt', 'r') as file:
        file.readline()
        log = file.readlines()
    return make_log_dict(log)


def append_log(log):
    with open('history.txt', 'a') as file:
        file.write(log)


def rewrite_log(log):
    with open('history.txt', 'w') as file:
        file.write(make_log_str(log))