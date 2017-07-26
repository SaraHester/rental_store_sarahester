##All functions go here
def make_list(inventory):
    list_inventory = []
    for line in inventory:
        item, price, quantity, value = inventory.split(', ')
        list_inventory.append(item.strip(), price.strip(), quantity.strip(), value.strip())
    return list_inventory
def make_dict(inventory)
    dict_inventory = {}
    for line in inventory:
        item, price, quantity, value = inventory.split(', ')
        dict_inventory[item] = {'name': item, 'price': price, 'quantity': quantity, 'value': value}
    return dict_inventory