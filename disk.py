#Opening and closing files goes here
import core
def open_log():
    with open('history.txt', 'r') as file:
        file.readline()
        log = file.readlines()
    return log

def append_log(i_d, name, time_out, time_in, total):
    with open('history.txt', 'a') as file:
        file.write('\n'+ str(i_d) + ', ' + str(name) + ', ' + str(time_out) +', ' + str(time_in) + ', ' + str(total))
def rewrite_checkin(dict_log, i_d, i_d_guess, time_in, total):
    with open('history.txt', 'w') as file:
        new_log = core.log_line()
        file.write(new_log)

def open_inventory():
    with open('inventory.txt', 'r') as file:
        file.readline()
        inventory = file.readlines()
    return inventory

def update_inventory(dict_inventory):
    with open('inventory.txt', 'w') as file:
        str_inventory = core.dict_inven_to_str(dict_inventory)
        file.write(str_inventory)

def check_out(dict_inventory, i_d,name, number, time_out):
    core.rent_out(dict_inventory, number)
    update_inventory(dict_inventory)
    append_log(i_d, name, time_out, 'N/A', 'N/A')
    
def check_in(dict_inventory, number, time_in, i_d, i_d_guess, deposit):
    core.rent_in(dict_inventory, number)
    update_inventory(dict_inventory)
    final_cost = core.final_cost(dict_inventory, number, days)
    rewrite_checkin(dict_log, i_d, i_d_guess, time_out, time_in, float(final_cost - deposit))
