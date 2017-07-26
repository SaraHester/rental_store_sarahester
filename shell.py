#Print and input go here
##Import core and disk
import core, disk, sys, random, time
##make helper functions
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/500)
def make_pretty(dict_inventory):
    number = 0
    for item in dict_inventory:
        number += 1
        phrase = "\n" + str(number) +'. '+ str(dict_inventory[item]['name']) + ':\n\tPrice per day: ' + str(dict_inventory[item]['price'])+' In stock: '+ str(dict_inventory[item]['quantity']) + ' Replacement value: '+ str(dict_inventory[item]['value'])
        for item in phrase:
            slow_type(item)

##make main
def main():
    inventory = disk.open_inventory()
    dict_inventory = core.make_dict(inventory)
    print("WELCOME to Game-Flix!!")
    #Start Branch
    answer = input('Are you a 1.customer or 2.employee?')
    if answer == '1':
        make_pretty(dict_inventory)
    elif answer == '2':
        print('OK')

if __name__=='__main__':
    main()