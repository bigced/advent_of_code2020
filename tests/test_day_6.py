from advent_of_code2020.day_6 import questions_group_anyone_answered_yes, sum_of_count, \
    questions_group_everyone_answered_yes


def test_parse_group_answer():
    data = """abcx
abcy
abcz"""
    assert questions_group_anyone_answered_yes(data) == 6

    data = """abc"""
    assert questions_group_anyone_answered_yes(data) == 3

    data = """a
b
c"""
    assert questions_group_anyone_answered_yes(data) == 3

    data = """a
a
a
a"""
    assert questions_group_anyone_answered_yes(data) == 1
    data = """b"""
    assert questions_group_anyone_answered_yes(data) == 1


def test_sum_of_anyone_count():
    data = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    assert sum_of_count(data, questions_group_anyone_answered_yes()) == 11

def test_sum_of_everyone_count():
        data = """abc

a
b
c

ab
ac

a
a
a
a

b"""
        assert sum_of_count(data, questions_group_everyone_answered_yes) == 6