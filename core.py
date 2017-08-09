# all logical functions go here


def update_dict_log(dict_log, i_d, name, time, total, rent_status):
    '''({dict}, str, str, str) -> {dict}'''
    dict_log[i_d] = {
        'id': i_d,
        'name': name,
        'time ': time,
        'total': 'N/A',
        'rent status': rent_status
    }
    return dict_log


def delete_from_inventory(dict_log, number):
    '''{dict}, int -> {dict}'''
    del dict_log[int(number)]
    return dict_log


def log_line(dict_log, i_d, rent_charge, days, time_in, total):
    '''{}, str, str, float -> {}'''
    dict_log[i_d]['time checked in'] = time_in
    dict_log[i_d]['total'] = total
    dict_log[i_d]['rent charge'] = rent_charge
    dict_log[i_d]['days'] = days
    return dict_log


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
    return cost + (cost * .07)


def final_cost(dict_inventory, number, days):
    '''{}, int, int -> int'''
    return rent_cost(
        dict_inventory, number,
        days) + sales_tax(rent_cost(dict_inventory, number, days))


def total_revenue(dict_log):
    revenue = 0
    for item in dict_log:
        revenue += float(dict_log[item]['total'])
    return revenue


def check(dict_log, i_d_guess):
    '''{}, str -> str'''
    for line in dict_log:
        if str(i_d_guess) == str(line):
            return True
    else:
        return False


def check_quantity(dict_inventory, number):
    '''{dict}, int -> bool'''
    if dict_inventory[number]['quantity'] > 0:
        return True
    else:
        return False


def change_inventory(dict_inventory, number, trait, new_trait):
    '''{dict}, int, str, str -> {dict}'''
    if trait == '1':
        dict_inventory[number]['name'] = new_trait
        return dict_inventory
    elif trait == '2':
        dict_inventory[number]['price'] = new_trait
        return dict_inventory
    elif trait == '3':
        dict_inventory[number]['quantity'] = new_trait
        return dict_inventory
    elif trait == '4':
        dict_inventory[number]['value'] = new_trait
        return dict_inventory