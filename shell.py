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

def input_answer():
    while True:
        answer = input('Are you a 1.customer or 2.employee?\n->')
        if answer == '1' or answer == '2':
            return answer
        else:
            print('Invalid Input')

def input_in_out():
    while True:
        in_out = input('Are you 1.checking out or 2.returning?\n->')
        if in_out == '1' or in_out == '2':
            return in_out
        else:
            print('Invalid Input')
def input_number():
    while True:
        choice = input('\nWhich one?\n->')
        if choice.isdigit():
            return choice
        else:
            print('Invalid Input')
def input_days():
    while True:
        days = input('How may days did you check it out?\n->')
        if days.isdigit() and int(days) < 10:
            return int(days)
        else:
            print('Sorry, either that\'s not a valid date or you can\'t rent it that many days')

def input_guess(dict_log, i_d):
    while True:
        i_d_guess = input('What is your log id?')
        if i_d_guess.isdigit() and core.check(dict_log, i_d, i_d_guess):
            return i_d_guess
        else:
            print('Sorry, That\'s not a valid id')
def input_password():
    password = '7D9n3'
    while True:
        password_guess = input('PLease enter the password\n->')
        if password_guess == password:
            return password
        else:
            print('\nINCORRECT PASSWORD\n')
##make main
def main():
    inventory = disk.open_inventory()
    dict_inventory = core.make_inven_dict(inventory)
    log = disk.open_log()
    dict_log = core.make_log_dict(log)
    print("WELCOME to Game-Flix!!")
    #Start Branch
    answer = input_answer()
    #customer
    if answer == '1':
        in_out = input_in_out()
        make_pretty_inventory(dict_inventory)
        
        #check oout
        if in_out == '1':
            number = input_number()
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
            number = input_number()
            days = input_days()
            i_d_guess = input_guess(dict_log)
            time_in = current_time()
            disk.check_in(dict_inventory, dict_log, number, time_in, i_d_guess,days)
            print('Your total is:', core.final_cost(dict_inventory, number, days))
    #employee
    elif answer == '2':
        input_password()
        option = input('What do you want to do? 1.Manage stock. 2. Check history 3. Add to inventory')
        if option == '1':
             make_pretty_inventory(dict_inventory)
        elif option == '2':
            make_pretty_log(dict_log)
        elif option ==- '3':
            name = input_name()
            price = input_price()
            quantity = input_quantity
            value = input_value()
            disk.append_inventory(number, name, price, quantity, value)

if __name__=='__main__':
    main()