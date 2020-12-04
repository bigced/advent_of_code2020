from unittest import mock

from advent_of_code2020.day_4 import parse_passport_option, extract_passport, number_of_item_validator, \
    validate_passport_batch, main, byr_validator, iyr_validator, eyr_validator, hgt_validator, hcl_validator, \
    ecl_validator, pid_validator


def test_parse_passport_options():
    data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm"""
    options = parse_passport_option(data)
    assert isinstance(options, dict)
    assert len(options) == 8


def test_extract_passport():
    data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

    passport_data = extract_passport(data)
    assert len(passport_data) == 4


def test_is_passport_valid_valid_8fields():
    data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm"""
    passport_options = parse_passport_option(data)
    assert number_of_item_validator(passport_options)

def test_is_passport_valid_invalid_missing_hgt():
    data = """iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929"""
    passport_options = parse_passport_option(data)
    assert False == number_of_item_validator(passport_options)


def test_multiple_passport():
    data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
    validators = [number_of_item_validator]
    assert validate_passport_batch(data, validators) == 2


def test_main_1():
    file_data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
    validators = [number_of_item_validator]
    mock_open = mock.mock_open(read_data=file_data)
    with mock.patch('builtins.open', mock_open):
        assert 2 == main('day_3.txt', validators)


def test_byr_validator():

    data = {"byr": "2002"}
    assert byr_validator(data)

    data = {"byr": "2003"}
    assert not byr_validator(data)


def test_iyr_validator():
    data = {"iyr": "2009"}
    assert not iyr_validator(data)

    data = {"iyr": "2021"}
    assert not iyr_validator(data)

    data = {"iyr": "2010"}
    assert iyr_validator(data)


def test_eyr_validator():
    data = {"eyr": "2009"}
    assert not eyr_validator(data)

    data = {"eyr": "2031"}
    assert not eyr_validator(data)

    data = {"eyr": "2021"}
    assert eyr_validator(data)


def test_hgt_validator():

    data =  {'hgt': '60in'}
    assert hgt_validator(data)

    data =  {'hgt': '190cm'}
    assert hgt_validator(data)

    data =  {'hgt': '190in'}
    assert not hgt_validator(data)

    data =  {'hgt': '190'}
    assert not hgt_validator(data)


def test_hcl_validator():
    data = {'hcl': "#123abc"}
    assert hcl_validator(data)

    data = {'hcl': '#123abz'}
    assert not hcl_validator(data)

    data = {'hcl': '123abc'}
    assert not hcl_validator(data)


def test_ecl_validator():
    data = {'ecl': 'brn'}
    assert ecl_validator(data)

    data = {'ecl': 'wat'}
    assert not ecl_validator(data)


def test_pid_validator():
    data = {'pid': "000000001"}
    assert pid_validator(data)

    data = {'pid': '0123456789'}
    assert not pid_validator(data)

def test_main_2():
    file_data = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
    validators = [number_of_item_validator, byr_validator, iyr_validator, eyr_validator, hgt_validator, hcl_validator,
                  ecl_validator, pid_validator]
    mock_open = mock.mock_open(read_data=file_data)
    with mock.patch('builtins.open', mock_open):
        assert main('day_3.txt', validators) == 4