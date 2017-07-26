# all logical functions go here
def make_inven_dict(inventory):
    dict_inventory = {}
    for line in inventory:
        number, item, price, quantity, value = line.split(', ')
        dict_inventory[int(number)] = {'number': number, 'name': item, 'price': float(price), 'quantity': int(quantity), 'value': float(value)}
    return dict_inventory
def dict_inven_to_str(dict_inventory):
    str_inventory = ''
    for item in dict_inventory:
        str_inventory += '\n' + str(dict_inventory[item]['number']) + ', ' + str(dict_inventory[item]['name']) + ', ' +  str(dict_inventory[item]['price']) + ', ' +  str(dict_inventory[item]['quantity']) + ', ' +  str(dict_inventory[item]['value'])
    return str_inventory
def make_log_dict(log):
    dict_log = {}
    for line in log:
        i_d, name, time_out, time_in, total = line.split(', ')
        dict_log[i_d] = {'name': name, 'time checked out': time_out , 'time checked in': time_in, 'total': total}
    return dict_log
def log_line(dict_log, i_d, i_d_guess, time_in, total):
    for number in dict_log:
        if i_d_guess == dict_log[i_d]:
            dict_log[i_d]['time checked in'] = time_in
            dict_log[i_d]['total'] = total
    return dict_log


def rent_out(dict_inventory, number):
    dict_inventory[number]['quantity'] -= 1
    return dict_inventory
def rent_cost(dict_inventory, number, days):
    return dict_inventory[number]['price'] * int(days)
def deposit(dict_inventory, number):
     return dict_inventory[number]['value'] * .10
def final_cost(dict_inventory, number, days):
    cost = deposit(dict_inventory, number) + rent_cost(dict_inventory, number, days) 
    return  cost +  sales_tax(cost)
def sales_tax(cost):
    return cost * .07