#Opening and closing files goes here
import core
def open_log():
    with open('history.txt', 'r') as file:
        file.readline()
        log = file.readlines()
    return log
def append_log(name, price, days):
    with open('history.txt', 'a') as file:
        file.write('\n'+ str(name) + ', ' + str(price) + ', ' + str(days))
def open_inventory():
    with open('inventory.txt', 'r') as file:
        file.readline()
        inventory = file.readlines()
    return inventory
def update_inventory(dict_inventory):
    with open('inventory.txt', 'w') as file:
        str_inventory = core.dict_to_str(dict_inventory)
        file.write(str_inventory)
def check_out(dict_inventory,name, number, days):
    core.rent_out(dict_inventory, number)
    update_inventory(dict_inventory)
    price = core.rent_cost(dict_inventory, number, days)
    append_log(name, price, days)
# def check_in(dict_inventory, number, time_in):
#     core.rent_in(dict_inventory, number)
#     update_inventory(dict_inventory)
#     append_log()
