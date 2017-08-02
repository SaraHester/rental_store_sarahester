#Opening and closing files goes here
import core
def open_inventory():
    with open('inventory.txt', 'r') as file:
        file.readline()
        inventory = file.readlines()
    return inventory

def append_inventory(text):
    with open('inventory.txt', 'a') as file:
        file.write(text)

def rewrite_inventory(text):
    with open('inventory.txt', 'w') as file:
        file.write(text)


def open_log():
    with open('history.txt', 'r') as file:
        file.readline()
        log = file.readlines()
    return log

def append_log(text):
    with open('history.txt', 'a') as file:
         file.write(text)

def rewrite_log(text):
    with open('history.txt', 'w') as file:
        file.write(text)