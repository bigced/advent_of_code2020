from unittest import mock

from advent_of_code2020.day_5 import decode_column_from_boarding_pass, split_row_data, decode_row_from_boarding_pass, \
    get_seat_id, main


def test_decode_row_from_boarding_pass():
    boarding_pass = "FBFBBFFRLR"
    assert 44 == decode_row_from_boarding_pass(boarding_pass)

    boarding_pass = 'BFFFBBFRRR'
    assert 70 == decode_row_from_boarding_pass(boarding_pass)

    boarding_pass = 'FFFBBBFRRR'
    assert 14 == decode_row_from_boarding_pass(boarding_pass)

    boarding_pass = 'BBFFBBFRLL'
    assert 102 == decode_row_from_boarding_pass(boarding_pass)


def test_decode_column_from_boarding_pass():
    boarding_pass = "FBFBBFFRLR"
    assert 5 == decode_column_from_boarding_pass(boarding_pass)

    boarding_pass = 'BFFFBBFRRR'
    assert 7 == decode_column_from_boarding_pass(boarding_pass)

    boarding_pass = 'FFFBBBFRRR'
    assert 7 == decode_column_from_boarding_pass(boarding_pass)

    boarding_pass = 'BBFFBBFRLL'
    assert 4 == decode_column_from_boarding_pass(boarding_pass)


def test_split_row_data_0_127_f():
    min_range = 0
    max_range = 127
    boarding_pass = 'FBFBBFFRLR'
    new_min_range, new_max_range, new_boarding_pass = split_row_data(min_range, max_range, boarding_pass)
    assert new_min_range == 0
    assert new_max_range == 63

    new_min_range, new_max_range, new_boarding_pass = split_row_data(new_min_range, new_max_range, new_boarding_pass)
    assert new_min_range == 32
    assert new_max_range == 63

    new_min_range, new_max_range, new_boarding_pass = split_row_data(new_min_range, new_max_range, new_boarding_pass)
    assert new_min_range == 32
    assert new_max_range == 47

    new_min_range, new_max_range, new_boarding_pass = split_row_data(new_min_range, new_max_range, new_boarding_pass)
    assert new_min_range == 40
    assert new_max_range == 47

    new_min_range, new_max_range, new_boarding_pass = split_row_data(new_min_range, new_max_range, new_boarding_pass)
    assert new_min_range == 44
    assert new_max_range == 47

    new_min_range, new_max_range, new_boarding_pass = split_row_data(new_min_range, new_max_range, new_boarding_pass)
    assert new_min_range == 44
    assert new_max_range == 45


def test_seat_id():
    row = 44
    column = 5
    assert get_seat_id(row, column) == 357


def test_seat_ids_from_boarding_passes():
    boarding_passes = [
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820)
    ]
    for bp, seat_id in boarding_passes:
        row = decode_row_from_boarding_pass(bp)
        column = decode_column_from_boarding_pass(bp)
        assert get_seat_id(row, column) == seat_id


def test_main_1():
    file_data = """FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""

    mock_open = mock.mock_open(read_data=file_data)
    with mock.patch('builtins.open', mock_open):
        assert 820 == main('day_5.txt')