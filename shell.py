##Import core and disk
import core, disk, sys, random, time, datetime, cool_letters


##helper functions
def print_intro():
    cool_letters.print_cool_letters('  Welcome To Game-Flix')


def random_i_d(dict_log):
    while True:
        i_d = ''
        choices = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        for i in range(8):
            i_d += random.choice(choices)
        if i_d != dict_log.keys():
            return str(i_d)


def current_time():
    return '{:%Y-%m-%d %H:%M}'.format(datetime.datetime.now())


def make_pretty_inventory(dict_inventory):
    for i in range(1, len(dict_inventory) + 1):
        print("\n" + str(dict_inventory[i]['number']) + '. ' +
              str(dict_inventory[i]['name']) + ':\n\tPrice per day: ' +
              str(dict_inventory[i]['price']) + ' In stock: ' +
              str(dict_inventory[i]['quantity']) + ' Replacement value: ' +
              str(dict_inventory[i]['value']))


def make_pretty_log(dict_log):
    for i in dict_log:
        msg = '\n ID: {}, Name: {}, \n\tTransaction time: {}, Total: {}, Rent Status: {}'.format(
            dict_log[i]['id'], dict_log[i]['name'], dict_log[i]['time'],
            dict_log[i]['total'], dict_log[i]['rent status'])
        print(msg)


def input_choice(number, string):
    while True:
        choice = input(string).strip()
        if choice.lower() == 'q':
            sys.exit()
        for i in range(1, number):
            if choice == str(i):
                return choice
        else:
            print(
                '----------------',
                '\n!Invalid Input!\n',
                '----------------',
                sep='')


def input_word(string):
    while True:
        word = input(string)
        if word.lower() == 'q':
            sys.exit()
        word2 = ''.join(character for character in word
                        if character not in ' :.!?()#&*%1234567890')
        if word2.isalpha():
            return str(word)
        else:
            print(
                '----------------',
                '\n!Invalid Input!\n',
                '----------------',
                sep='')


def input_int(string):
    while True:
        number = input(string).strip()
        if number.lower() == 'q':
            sys.exit()
        if number.isdigit() and int(number) > 0:
            return int(number)
        else:
            print(
                '----------------',
                '\n!Invalid Input!\n',
                '----------------',
                sep='')


def input_float(string):
    while True:
        number = input(string).strip()
        if number.lower() == 'q':
            sys.exit()
        if number.count('.') <= 1 and number.replace(
                '.', '').isnumeric() and float(number) > 0:
            return float(number)
        else:
            print(
                '----------------',
                '\n!Invalid Input!\n',
                '----------------',
                sep='')


def input_guess(dict_log, dict_inventory, number, string):
    while True:
        i_d_guess = input(string).strip()
        if i_d_guess.lower() == 'q':
            sys.exit()
        if core.check(
                dict_log, i_d_guess
        ) and dict_inventory[number]['name'] == dict_log[i_d_guess]['name']:
            return i_d_guess
        else:
            print(
                '---------------------------------------------------------------------------------------------------\n',
                '\nSorry, Either it\'s not a valid id or the id does not match any checked out movies with that name.\n',
                '----------------------------------------------------------------------------------------------------\n'
            )


def check_inven_or_log(dict_inventory, dict_log):
    revenue = core.total_revenue(dict_log)
    option = input(
        'What do you want to do? \n1.Manage stock. \n2. Check history\n3. Check revenue\n->'
    )
    if option == '1':
        make_pretty_inventory(dict_inventory)
    elif option == '2':
        make_pretty_log(dict_log)
    elif option == '3':
        print(revenue)


def add_to_inventory():
    name = input_word('\nWhat is the name of the item?\n->')
    price = input_float('\nWhat is the price of the item?\n->')
    quantity = input_int('\nHow many of this item do you have?\n->')
    value = input_float('\nWhat is the replacement value of this item?\n->')
    new_line = '\n' + str(name) + ', ' + str(price) + ', ' + str(
        quantity) + ', ' + str(value)
    disk.append_inventory(new_line)
    print('\n==Added to Inventory==\n')


def delete_from_inventory(dict_inventory):
    make_pretty_inventory(dict_inventory)
    number = int(
        input_choice(
            len(dict_inventory.keys()) + 1,
            '\nWhich item would you like to delete?\n->'))
    new_inventory = core.delete_from_inventory(dict_inventory, number)
    disk.rewrite_inventory(new_inventory)
    print('\n==Deleted from Inventory==\n')


def change_inventory(dict_inventory):
    number = int(
        input_choice(
            len(dict_inventory.keys()) + 1,
            '\nWhich item do you want to update?\n->'))
    trait = input_choice(
        5, '\n\n1. Name \n2.Price \n3.Quantity \n4.Replacement value\n->')
    if trait == '1':
        new_trait = input_word('\nWhat would you like to change it to?\n->')
    elif trait == '3':
        new_trait = input_int('\nWhat would you like to change it to?\n->')
    else:
        new_trait = input_float('\nWhat would you like to change it to?\n->')
    dict_inventory = core.change_inventory(dict_inventory, number, trait,
                                           new_trait)
    update_inventory(dict_inventory)
    print('\n==Inventory Changed==\n')


def update_inventory(dict_inventory):
    disk.rewrite_inventory(dict_inventory)


def append_log(dict_log, i_d, name, total, time, rent_status):
    new_line = '\n{}, {}, {}, {}, {}'.format(i_d, name, time, total,
                                             rent_status)
    disk.append_log(new_line)


def clear_log():
    disk.rewrite_log('')


def rent_out(dict_inventory, dict_log, i_d, name, number, total, time):
    core.rent_out(dict_inventory, number)
    update_inventory(dict_inventory)
    append_log(dict_log, i_d, name, total, time, 'check_out')


def check_out(dict_inventory, dict_log):
    number = int(
        input_choice(
            len(dict_inventory.keys()) + 1,
            "\nWhich one would you like to check out\n->"))
    i_d = random_i_d(dict_log)
    name = dict_inventory[number]['name']
    time = current_time()
    if core.check_quantity(dict_inventory, number):
        deposit = core.deposit(dict_inventory, number)
        dict_log = core.update_dict_log(dict_log, i_d, name, deposit, time,
                                        'check_out')
        rent_out(dict_inventory, dict_log, i_d, name, number, deposit, time)
        receipt(i_d, dict_log, dict_inventory, number, deposit, time,
                'check_out')
    else:
        print('\nSorry, were out of that item\n')


def returning(dict_inventory, dict_log, number, time, i_d_guess, total):
    core.rent_in(dict_inventory, number)
    update_inventory(dict_inventory)
    name = dict_inventory[number]['name']
    append_log(dict_log, i_d_guess, name, total, time, 'check_in')


def check_in(dict_inventory, dict_log):
    number = int(
        input_choice(
            len(dict_inventory.keys()) + 1,
            '\nWhich one are you returning?\n->'))
    days = input_int('\nHow many days did you rent it?\n->')
    i_d_guess = input_guess(dict_log, dict_inventory, number,
                            '\nWhat is your id number?(enter q to quit)\n->')
    time = current_time()
    final_cost = core.final_cost(dict_inventory, number, days)
    returning(dict_inventory, dict_log, number, time, i_d_guess, final_cost)
    receipt(i_d_guess, dict_log, dict_inventory, number, final_cost, time,
            'check_out')


def admin(dict_inventory):
    print('Main Menu')
    option = input_choice(
        5,
        '\n1. Add to inventory \n2. Delete from inventory \n3. Change or update inventory \n4. Clear history\n->'
    )
    if option == '1':
        add_to_inventory()
    elif option == '2':
        delete_from_inventory(dict_inventory)
    elif option == '3':
        make_pretty_inventory(dict_inventory)
        change_inventory(dict_inventory)
    elif option == '4':
        clear = input_choice(
            3, '\nAre you sure you want to clear\n 1. Yes  2.No\n->')
        if clear == '1':
            clear_log()
            print("\n==History Cleared==\n")
        else:
            print("\nRequest Denied. Exiting...\n")


def random_barcode_lines(length, height):
    '''int-> str'''
    choices = "▎", "▍", "▌", "█", "▌", "▌"
    code = []
    for i in range(length):
        code.append(random.choice(choices))
    return ''.join(code)


def rand_numbers(length):
    numbers = "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
    code = []
    for i in range(length):
        code.append(random.choice(numbers))
    line = ''.join(code)
    return '\n║\t   ║'.join(line for _ in range(1))


def receipt(i_d, dict_log, dict_inventory, number, total, time, rent_status):
    '''str, float, float, str -> str'''
    code = random_barcode_lines(20, 2)
    print("\tHere is your receipt.\n\t😄Have a good day!😄\n")
    cool_letters.print_cool_letters('Game-Flix')
    print("\t╔══════════════════════════════════════════════╗")
    print("\t║                   GAME-FLIX                  ║")
    print("\t║----------------------------------------------║")
    print("\t║Item:",
          str(dict_inventory[number]['name']).ljust(
              51 - len(str(dict_inventory[number]['name']))), "║")
    print("\t║Price per day:",
          str(dict_inventory[number]['price']).ljust(
              33 - len(str(dict_inventory[number]['price']))), "║")
    print("\t║Sales Tax: 0.07                               ║")
    print("\t║Total sales: {0:.2f}".format(total)), ''.ljust(
        31 - len(str(total)), "║")
    print("\t║ID number:", str(i_d), ''.ljust(47 - len(str(id))), "║")
    print("\t║Time:", str(time), ''.ljust(32), "║")
    print("\t║Rent Status: ", str(rent_status))
    print("\t║----------------------------------------------║")
    print("\t║          ", code, "            ║")
    print("\t║          ", code, "            ║")
    print("\t║          ", rand_numbers(20), "              ║")
    print("\t║                                              ║")
    print("\t║                                              ║")
    print("\t║==============================================║")
    print("\t║                                              ║")
    print("\t║EARN YOUR CHANCE AT $500!!!!!                 ║")
    print("\t║`just go to the link below`                   ║")
    print("\t║www.earnfreemoney.org                         ║")
    print("\t║==============================================║")
    print("\t╚══════════════════════════════════════════════╝")
    print("\n")


###MAIN##
def main():
    dict_inventory = disk.open_inventory()
    dict_log = disk.open_log()
    print_intro()
    answer = input_choice(
        4,
        '\nAre you \n1. customer \n2. Employee \n3. Administrator?\n(Enter q to quit at any time)\n->'
    )

    if answer == '1':
        in_out = input_choice(
            3, '\nAre you \n1. checking out \n2. returning?\n->')
        make_pretty_inventory(dict_inventory)
        if in_out == '1':
            check_out(dict_inventory, dict_log)
        elif in_out == '2':
            check_in(dict_inventory, dict_log)

    elif answer == '2':
        check_inven_or_log(dict_inventory, dict_log)

    elif answer == '3':
        admin(dict_inventory)


if __name__ == '__main__':
    main()