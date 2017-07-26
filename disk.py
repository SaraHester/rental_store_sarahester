#Opening and closing files goes here
import core
def open_log():
    with open('history.txt', 'r') as file:
        file.readline()
        log = file.readlines()
    return log
def append_log(name, price, time_out, time_in):
    with open('history.txt', 'a') as file:
        file.write('\n'+ name + ', ' + price + ', ' + time_out + ', ' + time_in)
def open_inventory():
    with open('inventory.txt', 'r') as file:
        file.readline()
        inventory = file.readlines()
    return inventory
def update_inventory(dict_inventory):
    with open('inventory.txt', 'w') as file:
        str_inventory = core.dict_to_str(inventory)
        file.write(str_inventory)

