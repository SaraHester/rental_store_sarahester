#Print and input go here
##Import core and disk
import core, disk, sys, random, time, datetime
##make helper functions
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/500)
def make_pretty(dict_inventory):
    for i in range(1,len(dict_inventory) + 1):
        phrase = "\n" + str(dict_inventory[i]['number']) +'. '+ str(dict_inventory[i]['name']) + ':\n\tPrice per day: ' + str(dict_inventory[i]['price'])+' In stock: '+ str(dict_inventory[i]['quantity']) + ' Replacement value: '+ str(dict_inventory[i]['value'])
        for item in phrase:
            slow_type(item)
def random_i_d(dict_log):
    while True:
        i_d = ''
        choices = '0','1','2','3','4', '5', '6', '7', '8', '9'
        for i in range(8):
            i_d += random.choice(choices)
        if i_d != dict_log.keys():
            return i_d
def current_time():
    return datetime.datetime.now()
##make main
def main():
    inventory = disk.open_inventory()
    dict_inventory = core.make_inven_dict(inventory)
    log = disk.open_log()
    dict_log = core.make_log_dict(log)
    print("WELCOME to Game-Flix!!")
    #Start Branch
    answer = input('Are you a 1.customer or 2.employee?\n->')
    #customer
    if answer == '1':
        in_out = input('Are you 1.checking out or 2.returning?')
        make_pretty(dict_inventory)
        number = int(input('Which one?\n->'))
        #check oout
        if in_out == '1':
            i_d = random_i_d(dict_log)
            name = dict_inventory[number]['name']
            time_out = current_time()
            disk.check_out(dict_inventory, i_d, name, number, time_out)
            print('item checked out:', name)
            print('The deposit is:', core.deposit(dict_inventory, number))
            print('Thank you. Your log id number is', i_d)
        # check in
        elif in_out =='2':
            #make helper function
            days = input('How may days did you check it out?\n->')
            i_d_guess = input('What is your log id?')
            i_d_guess = core.check(dict_log, i_d_guess)
            time_in = current_time()
            disk.check_in(dict_inventory, dict_log, number, time_in, i_d_guess,days)
            print('Your total is:', core.final_cost(dict_inventory, number, days))
    #employee
    elif answer == '2':
        option = input('What do you want to do? 1.Manage stock. 2. Check history')
        if option == '1':
            print(log)
        elif option == '2':
            make_pretty(dict_inventory)

if __name__=='__main__':
    main()