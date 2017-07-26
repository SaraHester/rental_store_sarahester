# all logical functions go here
def make_dict(inventory):
    dict_inventory = {}
    for line in inventory:
        item, price, quantity, value = line.split(', ')
        dict_inventory[item] = {'name': item, 'price': price, 'quantity': quantity, 'value': value}
    return dict_inventory