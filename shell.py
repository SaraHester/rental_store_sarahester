#Print and input go here
##Import core and disk
import core, disk, sys, random, time, datetime, cool_letters
##make helper functions
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/500)
def print_intro():
    cool_letters.print_cool_letters('Welcome To Game-Flix')
def make_pretty_inventory(dict_inventory):
    for i in range(1,len(dict_inventory) + 1):
        print("\n" + str(dict_inventory[i]['number']) +'. '+ str(dict_inventory[i]['name']) + ':\n\tPrice per day: ' + str(dict_inventory[i]['price'])+' In stock: '+ str(dict_inventory[i]['quantity']) + ' Replacement value: '+ str(dict_inventory[i]['value']))

def make_pretty_log(dict_log):
    for i in range(1,len(dict_log) + 1):
        print('\n' + str(dict_log[i]['number']) + ', ' +  str(dict_log[i]['id']) + 'Name: ' + str(dict_log[i]['Name'] + 'Time checked out:' + str(dict_log[i]['time checked out'])) + 'Time checked in:' + str(dict_log[i]['time checked out']) + 'Total:' + str(dict_log[i]['total']))

def random_i_d(dict_log):
    while True:
        i_d = ''
        choices = '0','1','2','3','4', '5', '6', '7', '8', '9'
        for i in range(8):
            i_d += random.choice(choices)
        if i_d != dict_log.keys():
            return str(i_d)
def current_time():
    return '{:%Y-%m-%d %H:%M}'.format(datetime.datetime.now())



def input_choice(number, string):
    while True:
        choice = input(string)
        for i in range(number):
            if choice == str(i):
                return choice
        else:
            print('Invalid Input')

def input_word(string):
    while True:
        word = input(string)
        if word.isalpha():
            return word
        else:
            print('Invalid Name')

def input_int(string):
    while True:
        number = input(string)
        if number.isdigit():
            return int(number)
        else:
            print('Invalid Input')
def input_float(string):
    while True:
        number = input(string)
        if number.count('.') == 1:
            number.remove('.')
            if number.isdigit:
                return number
        else:
            print('Invalid Input')

def input_guess(dict_log, string):
    while True:
        i_d_guess = input(string)
        if core.check(dict_log,i_d_guess):
            return i_d_guess
        else:
            print('Sorry, That\'s not a valid id')

def input_password(password):
    while True:
        password_guess = input('PLease enter the password\n->')
        if password_guess == password:
            return password
        else:
            print('\nINCORRECT PASSWORD\n')

def check_inven_or_log(dict_inventory, dict_log):
        option = input('What do you want to do? 1.Manage stock. 2. Check history\n->')
        if option == '1':
             make_pretty_inventory(dict_inventory)
        elif option == '2':
            make_pretty_log(dict_log)
def add_to_inventory():
    name = input_word('What is the name of the item?\n->')
    price = input('What is the price of the item?\n')
    quantity = input_int('How many of this item do you have?\n->')
    value = input('What is the replacement value of this item?\n->')
    disk.append_inventory(name, price, quantity, value)
def change_inventory(dict_inventory):
    status = ''
    while status != '2':
        number = input_int('Which item do you want to update?\n->')
        trait = input_choice(4, '1. Name 2.Price 3. Replacement value')
        if trait == '1':
            new_trait = input_word('What would you like to change it to?\n->')
        else:
            new_trait = input_float('What would you like to change it to?\n->')
        dict_inventory = core.change_inventory(dict_inventory, number, trait, new_trait)
        disk.update_inventory(dict_inventory)
        status = input_choice(3, '1. Change something else, 2. Go back to Main Menu\n->')
def random_barcode_lines(length, height):
    '''int-> str'''
    choices =  "▎", "▏", "▍", "▌", "█", "▌", "▌"
    code = []
    for i in range(length):
        code.append(random.choice(choices))
    return''.join(code)
    


def rand_numbers(length):
    numbers = "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
    code = []
    for i in range(length):
        code.append(random.choice(numbers))
    line = ''.join(code)
    return '\n║\t   ║'.join(line for _ in range(1))

def receipt(i_d, dict_log, dict_inventory, number, date):
    '''str, float, float, str -> str'''
    code = random_barcode_lines(20, 2)
    print("\tHere is your receipt.\n\t😄Have a good day!😄")
    print("\n")
    cool_letters.print_cool_letters('Game-Flix')
    print("\t╔══════════════════════════════════════════════╗")
    print("\t║                   GAME-FLIX                  ║")
    print("\t║----------------------------------------------║")
    print("\t║Item:", str(dict_inventory[number]['name']).ljust(10 - len(str(dict_inventory[number]['name']))), "║")
    print("\t║Price per day:", str(dict_inventory[number]['price']).ljust(33 - len(str(dict_inventory[number]['price']))), "║")
    print("\t║Days checked out:", str(dict_log[i_d]['days']).ljust(29 - len(str(dict_log[i_d]['days']))), "║")
    print("\t║Rent Charge:", str(dict_log[i_d]['rent charge']), "".ljust(31 - len(str(dict_log[i_d]['rent charge']))), "║")
    print("\t║Sales Tax: 0.07                               ║")
    print("\t║Total sales:", str(dict_log[i_d]['total']) , ''.ljust(31 - len(str(dict_log[i_d]['total']))), "║" )
    print("\t║Time checked out:", str(dict_log[i_d]['time checked out']), "".ljust(26 - len(str(dict_log[i_d]['time checked out']))), "║")
    print("\t║Time checked in:", str(dict_log[i_d]['time checked in']), "".ljust(27 - len(str(dict_log[i_d]['time checked in']))), "║")
    print("\t║Transaction time:", date, "".ljust(10), "║" )
    print("\t║----------------------------------------------║" )
    print("\t║            ",code, "            ║")
    print("\t║            ",code, "            ║")
    print("\t║            ",rand_numbers(20),"            ║")
    print("\t║                                              ║")
    print("\t║                                              ║")
    print("\t║==============================================║")
    print("\t║                                              ║" )
    print("\t║EARN YOUR CHANCE AT $500!!!!!                 ║")
    print("\t║`just go to the link below`                   ║" )
    print("\t║www.earnfreemoney.org                         ║" )
    print("\t║==============================================║" )
    print("\t╚══════════════════════════════════════════════╝")
    print("\n")

##make main
def main():
    inventory = disk.open_inventory()
    dict_inventory = core.make_inven_dict(inventory)
    log = disk.open_log()
    dict_log = core.make_log_dict(log)
    print_intro()
    #Start Branch
    answer = input_choice(4, 'Are you 1. customer 2. Employee 3. Administrator?\n->')
    #customer
    if answer == '1':
        in_out = input_choice(3, 'Are you 1. checking out 2. returning?\n->')
        make_pretty_inventory(dict_inventory)
        #check oout
        if in_out == '1':
            number = input_int("Which one would you like to check out\n->")
            i_d = random_i_d(dict_log)
            name = dict_inventory[number]['name']
            time_out = current_time()
            if core.check_quantity(dict_inventory) > 1:
                disk.check_out(dict_inventory, i_d, name,number, time_out)
                dict_log = core.update_dict_log(dict_log, i_d, name, time_out)
                receipt(i_d, dict_log, dict_inventory, number, time_out)
            else:
                print('Sorry, were out of that item')
        # check in
        elif in_out =='2':
            #make helper function
            number = input_int('Which one are you returning?\n->')
            days = input_int('How many days did you rent it?\n->')
            i_d_guess = input_guess(dict_log, 'What is your id number?\n->')
            time_in = current_time()
            disk.check_in(dict_inventory, dict_log, number, time_in, i_d_guess, days)
            receipt(i_d_guess, dict_log, dict_inventory, number, time_in)
    #employee
    elif answer == '2':
        input_password('no')
        check_inven_or_log(dict_inventory, dict_log)

    elif answer == '3':
            print('Main Menu')
            option = input_choice(4, '1. Add to inventory 2. Change or update inventory 3. Clear log')
            if option == '1':
                add_to_inventory()
            elif option == '2':
                make_pretty_inventory(dict_inventory)
                change_inventory(dict_inventory)
            elif option == '3':
                clear = input_choice(3, 'Are you sure you want to clear\n 1. Yes  2.No\n->')
                if clear == '1':
                    disk.clear_log()
                else:
                    print('Ok. Is there anything else you want to do?')
                    

if __name__=='__main__':
    main()