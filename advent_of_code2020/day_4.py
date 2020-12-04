import re


def parse_passport_option(data):
    options = {}
    for option in data.split():
        key, value = option.split(':')
        options[key] = value
    return options


def extract_passport(data):
    return data.split('\n\n')


def number_of_item_validator(options):
    required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    options_set = set(options.keys())
    missing_options = required - options_set
    return len(missing_options) == 0


def validate_passport_batch(data, validators):
    passports = extract_passport(data)
    count = 0
    for passport in passports:
        options = parse_passport_option(passport)
        is_valid = 0
        for validator in validators:
            try:
                if validator(options):
                    is_valid += 1
            except:
                break
        count += is_valid == len(validators)

    # valids = [number_of_item_validator(parse_passport_option(p)) for p in passports]
    return count


def main(filename, validators):
    with open(filename, 'r') as f:
        data = f.read()
    return validate_passport_batch(data, validators)

def byr_validator(data):
    value = int(data.get('byr'))
    return 1920 <= value <= 2002


def iyr_validator(data):
    value = int(data.get('iyr'))
    return 2010 <= value <= 2020


def eyr_validator(data):
    value = int(data.get('eyr'))
    return 2020 <= value <= 2030


def hgt_validator(data):
    value = data.get('hgt')
    if 'cm' not in value and 'in' not in value:
        return False
    if 'cm' in value:
        return 150 <= int(value.replace('cm', '')) <= 193
    return 59 <= int(value.replace('in', '')) <= 76


def hcl_validator(data):
    value = data['hcl']
    pattern = re.compile("\#[a-f0-9]+")
    return pattern.fullmatch(value) is not None


def ecl_validator(data):
    value = data['ecl']
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid_validator(data):
    value = data['pid']
    pattern = re.compile("^\d{9}$")
    return pattern.fullmatch(value) is not None


if __name__ == '__main__':
    validators = [number_of_item_validator]
    print(main('day_4.txt', validators))

    validators = [number_of_item_validator, byr_validator, iyr_validator, eyr_validator, hgt_validator, hcl_validator,
                  ecl_validator, pid_validator]
    print(main('day_4.txt', validators))


