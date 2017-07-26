# all logical functions go here
def make_dict(inventory):
    dict_inventory = {}
    for line in inventory:
        item, price, quantity, value = line.split(', ')
        dict_inventory[item] = {'name': item, 'price': price, 'quantity': quantity, 'value': value}
    return dict_inventory
def dict_to_str(dict_inventory):
    str_inventory = ''
    for item in dict_inventory:
        str_inventory += str(dict_inventory[item]['name']) + str(dict_inventory[item]['price']) + str(dict_inventory[item]['quantity']) + str(dict_inventory[item]['value'])
    return str_inventory
def rent(dict_inventory, name):
    dict_inventory[name]['quantity'] -= 1
    disk.update_inventory(dict_inventory)


