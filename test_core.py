import core

def test_make_inven_dict():
    inventory = ['1, Call of Duty, 3.0, -9, 35.0\n', '2, Deadman Wonderland(season 1), 5.0, -13, 45.0\n', '3, Need for Speed:Most Wanted, 2.05, 8, 24.0']
    assert core.make_inven_dict(inventory) == {
        1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': -13, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }
def test_dict_ineven_to_str():
    inventory = {
        1: {'quantity': -9, 'number': '1', 'price': 3.0, 'value': 35.0, 'name': 'Call of Duty'}, 
        2: {'quantity': -13, 'number': '2', 'price': 5.0, 'value': 45.0, 'name': 'Deadman Wonderland(season 1)'},
        3: {'quantity': 8, 'number': '3', 'price': 2.05, 'value': 24.0, 'name': 'Need for Speed:Most Wanted'}
        }
    assert core.dict_inven_to_str(inventory) == '\n1, Call of Duty, 3.0, -9, 35.0\n2, Deadman Wonderland(season 1), 5.0, -13, 45.0\n3, Need for Speed:Most Wanted, 2.05, 8, 24.0'
def test_make_log_dict():
    log = ['84742666, Deadman Wonderland(season 1), 2017-07-27 11:06:12.902951, N/A, N/A\n', '04470289, Call of Duty, 2017-07-27 11:06:43.142199, 2017-07-27 11:07:29.249265, 16.295\n', '44030379, Call of Duty, 2017-07-27 11:06:18.614966, N/A, N/A']
    assert core.make_log_dict(log) == {
        '04470289': {'time checked out': '2017-07-27 11:06:43.142199', 'total': '16.295\n', 'name': 'Call of Duty', 'id': '04470289', 'time checked in': '2017-07-27 11:07:29.249265'}, 
        '44030379': {'time checked out': '2017-07-27 11:06:18.614966', 'total': 'N/A', 'name': 'Call of Duty', 'id': '44030379', 'time checked in': 'N/A'}, 
        '84742666': {'time checked out': '2017-07-27 11:06:12.902951', 'total': 'N/A\n', 'name': 'Deadman Wonderland(season 1)', 'id': '84742666', 'time checked in': 'N/A'}
        }