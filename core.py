# all logical functions go here
def make_dict(inventory):
    dict_inventory = {}
    for line in inventory:
        number, item, price, quantity, value = line.split(', ')
        dict_inventory[int(number)] = {'number': number, 'name': item, 'price': float(price), 'quantity': int(quantity), 'value': float(value)}
    return dict_inventory
def dict_to_str(dict_inventory):
    str_inventory = ''
    for item in dict_inventory:
        str_inventory += '\n' + str(dict_inventory[item]['number']) + ', ' + str(dict_inventory[item]['name']) + ', ' +  str(dict_inventory[item]['price']) + ', ' +  str(dict_inventory[item]['quantity']) + ', ' +  str(dict_inventory[item]['value'])
    return str_inventory
def rent(dict_inventory, number):
    dict_inventory[number]['quantity'] -= 1
    return dict_inventory




