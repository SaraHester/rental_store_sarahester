#Print and input go here
##Import core and disk
import core, disk, sys, random, time, datetime
##make helper functions
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/500)
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
            return i_d
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

def input_number(string):
    while True:
        number = input(string)
        if number.isdigit():
            return int(number)
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
    quantity = input_number('How many of this item do you have?\n->')
    value = input('What is the replacement value of this item?\n->')
    disk.append_inventory(name, price, quantity, value)
##make main
def main():
    inventory = disk.open_inventory()
    dict_inventory = core.make_inven_dict(inventory)
    log = disk.open_log()
    dict_log = core.make_log_dict(log)
    print("WELCOME to Game-Flix!!")
    #Start Branch
    answer = input_choice(4, 'Are you 1. customer 2. Employee 3. Administrator?\n->')
    #customer
    if answer == '1':
        in_out = input_choice(3, 'Are you 1. checking out 2. returning?\n->')
        make_pretty_inventory(dict_inventory)
        
        #check oout
        if in_out == '1':
            number = input_number("Which one would you like to check out\n->")
            i_d = random_i_d(dict_log)
            name = dict_inventory[number]['name']
            time_out = current_time()
            if core.check_quantity(dict_inventory) > 1:
                disk.check_out(dict_inventory, i_d, name, number, time_out)
                print('item checked out:', name)
                print('The deposit is:', core.deposit(dict_inventory, number))
                print('Thank you. Your log id number is', i_d)
            else:
                print('Sorry, were out of that item')
        # check in
        elif in_out =='2':
            #make helper function
            print(dict_inventory)
            print(dict_log)
            number = input_number('Which one are you returning?\n->')
            days = input_number('How many days did you rent it?\n->')
            i_d_guess = input_guess(dict_log, 'What is your id number?\n->')
            time_in = current_time()
            disk.check_in(dict_inventory, dict_log, number, time_in, i_d_guess, days)
            print('Your total is:', core.final_cost(dict_inventory, number, days))
    #employee
    elif answer == '2':
        input_password('no')
        check_inven_or_log(dict_inventory, dict_log)

    elif answer == '3':
            option = input_choice(3, '1. Add to inventory 2. Change or update inventory 3. Clear log')
            if option == '1':
                add_to_inventory()
if __name__=='__main__':
    main()