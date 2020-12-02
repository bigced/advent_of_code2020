from unittest import mock

from advent_of_code2020.day_2 import read_password, check_password_nb_occurence, get_data_from_file, main, \
    check_password_occurence_position


def test_chec_nb_occ_passwords():
    data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
    passwords = read_password(data)
    assert check_password_nb_occurence(passwords[0]) == True
    assert check_password_nb_occurence(passwords[1]) == False
    assert check_password_nb_occurence(passwords[2]) == True


def test_check_occurence_position_passwords():
    data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
    passwords = read_password(data)
    assert check_password_occurence_position(passwords[0]) == True
    assert check_password_occurence_position(passwords[1]) == False
    assert check_password_occurence_position(passwords[2]) == False


def test_get_data_from_file():
    file_data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
    mock_open = mock.mock_open(read_data=file_data)
    with mock.patch('builtins.open', mock_open):
        data = get_data_from_file('day_2.txt')
        mock_open.assert_called_once_with('day_2.txt')


@mock.patch('builtins.print')
def test_main(mocked_print):
    file_data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
    mock_open = mock.mock_open(read_data=file_data)
    with mock.patch('builtins.open', mock_open):
        main('day_2.txt', check_password_nb_occurence)
        mocked_print.assert_called_once_with(2)

        main('day_2.txt', check_password_occurence_position)
    assert mocked_print.call_args_list[0].args[0] == 2
    assert mocked_print.call_args_list[1].args[0] == 1
