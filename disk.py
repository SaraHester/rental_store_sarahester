#Opening and closing files goes here
def open_log():
    with open('history.txt', 'r') as file:
        file.readline()
        log = file.readlines()
    return log
# def append_log():
def open_inventory():
    with open('inventory.txt', 'r') as file:
        file.readline()
        inventory = file.readlines()
    return inventory
# def append_inventory():