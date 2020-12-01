from advent_of_code2020.day_1 import get_two_entries_that_sums_2020, multiply_element, get_three_entries_that_sums_2020


def test_day_1_two_numbers_eq_2020():
    data = [1721, 979, 366, 299, 675, 1456]

    entries = get_two_entries_that_sums_2020(data)
    assert sorted(entries) == [299, 1721]

    result = multiply_element(entries)
    assert result == 514579

def test_day_1_two_numbers_eq_2020():
    data = [1721, 979, 366, 299, 675, 1456]

    entries = get_three_entries_that_sums_2020(data)
    assert sorted(entries) == [366, 675, 979]

    result = multiply_element(entries)
    assert result == 241861950