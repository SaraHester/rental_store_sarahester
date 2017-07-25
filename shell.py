#Print and input go here
##Import core and disk
import core, disk
##make helper functions
##make main
def print_cool_letters(letters):
    blocks = map(core.find_cool_letters, letters)
    print('\n'.join(map('\t'.join, zip(*blocks))))
def main():
print("WELCOME to Game-Flix!!")
answer = input('Are you a 1.customer or 2.employee?')
if answer == '1':
    #show inventory
elif answer == '2':
    #ask for password

if __name__='__main__':
    main()