import core

def test_make_inven_dict():
    inventory = ['Call of Duty, 3.0, -9, 35.0\n','Deadman Wonderland(season 1), 5.0, -13, 45.0\n', 'Need for Speed:Most Wanted, 2.05, 8, 24.0']
    assert core.make_inven_dict(inventory) == {
        1: {'quantity': -9, 'number': 1, 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': -13, 'number': 2, 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': 3, 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }
def test_dict_ineven_to_str():
    inventory = {
        1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': -13, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }
    assert core.dict_inven_to_str(inventory) == '\nCall of Duty, 3.0, -9, 35.0\nDeadman Wonderland(season 1), 5.0, -13, 45.0\nNeed for Speed:Most Wanted, 2.05, 8, 24.0'

def test_make_log_dict():
    log = ['84742666, Deadman Wonderland(season 1), N/A, N/A, 2017-07-27 11:06:12.902951, N/A, N/A']
    assert core.make_log_dict(log) == {
        '84742666': {'time checked out': '2017-07-27 11:06:12.902951', 'total': 'N/A', 'name': 'Deadman Wonderland(season 1)', 'id': '84742666', 'time checked in': 'N/A', 'rent charge': 'N/A', 'days': 'N/A' }}

def test_make_log_str():
    log = {'04470289': {'time checked out': '2017-07-27 11:06:43.142199', 'total': 16.295, 'name': 'Call of Duty', 'id': '04470289', 'time checked in': '2017-07-27 11:07:29.249265', 'days': 5, 'rent charge': 13.4}}
    assert core.make_log_str(log) == '\n04470289, Call of Duty, 5, 13.4, 2017-07-27 11:06:43.142199, 2017-07-27 11:07:29.249265, 16.295'

def test_update_dict_log():
    log = {}
    assert core.update_dict_log(log, '04470289','Call of Duty', '2017-07-27 11:07:29.249265') == {'04470289': {'time checked out': '2017-07-27 11:07:29.249265', 'total': 'N/A', 'name': 'Call of Duty', 'id': '04470289', 'time checked in': 'N/A', 'days': 'N/A', 'rent charge': 'N/A'}}


def test_log_line():
    dict_log ={
        '44030379': {'time checked out': '2017-07-27 11:06:43.142199', 'total': 'N/A', 'name': 'Call of Duty', 'id': '04470289', 'time checked in': 'N/A', 'days': 'N/A', 'rent charge': 'N/A'}, 
        '04470289': {'time checked out': '2017-07-27 11:06:43.142199', 'total': 16.295, 'name': 'Call of Duty', 'id': '04470289', 'time checked in': '2017-07-27 11:07:29.249265', 'days': 5, 'rent charge': 13.4}}
    assert core.log_line(dict_log, '44030379', 5.4, 6, '2017-07-27 11:06:12.90295', 40) == {
        '44030379': {'time checked out': '2017-07-27 11:06:43.142199', 'total': 40, 'name': 'Call of Duty', 'id': '04470289', 'time checked in': '2017-07-27 11:06:12.90295', 'days': 6, 'rent charge': 5.4}, 
        '04470289': {'time checked out': '2017-07-27 11:06:43.142199', 'total': 16.295, 'name': 'Call of Duty', 'id': '04470289', 'time checked in': '2017-07-27 11:07:29.249265', 'days': 5, 'rent charge': 13.4}
        }
def test_new_line():
    assert core.new_line('Alice in Wonderland', 3.4, 24, 12) == '\nAlice in Wonderland, 3.4, 24, 12'

def test_rent_out():
    inventory = {
        1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': -14, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }
    assert core.rent_out(inventory, 2) == {
        1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': -15, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }

def test_rent_in():
    inventory = {
        1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': 20, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }
    assert core.rent_in(inventory, 2) == {
        1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': 21, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }

def test_rent_cost():
    inventory = {
        1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': 20, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }
    assert core.rent_cost(inventory, 2, 5) == 25

def test_deposit():
    inventory = {
        1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': 20, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }
    assert core.deposit(inventory, 2) == 4.5

def test_sales_tax():
    assert core.sales_tax(29.5) == 2.0650000000000004

def test_final_cost():
    inventory = {
        1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': 20, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }
    assert core.final_cost(inventory, 2, 5) == 31.565

def test_check():
    dict_log ={
        '04470289': {'time checked out': '2017-07-27 11:06:43.142199', 'total': '16.295', 'name': 'Call of Duty', 'id': '04470289', 'time checked in': '2017-07-27 11:07:29.249265'}, 
        '44030379': {'time checked out': '2017-07-27 11:06:18.614966', 'total': 'N/A', 'name': 'Call of Duty', 'id': '44030379', 'time checked in': 'N/A'}, 
        '84742666': {'time checked out': '2017-07-27 11:06:12.902951', 'total': 'N/A', 'name': 'Deadman Wonderland(season 1)', 'id': '84742666', 'time checked in': 'N/A'}
        }
    assert core.check(dict_log, '44030379') == True
    assert core.check(dict_log, '4403037') == False
    assert core.check(dict_log, '77667565') == False

def test_check_quantity():
    inventory = {
        1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': 20, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }
    assert core.check_quantity(inventory) == 0

    inventory2 = {
        1: {'quantity': 9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': 20, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }
    assert core.check_quantity(inventory2) == 3

def test_change_inventory():
    inventory = {1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}}
    assert core.change_inventory(inventory, 1, '1', 'COD') == {1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'COD'}}
    assert core.change_inventory(inventory, 1, '2', 4) == {1: {'quantity': -9, 'number': '1', 'price': 4.0, 'value': 35.0, 'name': 'COD'}}
    assert core.change_inventory(inventory, 1, '3', 34) == {1: {'quantity': -9, 'number': '1', 'price': 4.0, 'value': 34.0, 'name': 'COD'}}
    assert core.change_inventory(inventory, 1, '4', 34) ==  None