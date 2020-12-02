def read_password(data):
    return data.split('\n')


def check_password_nb_occurence(param):
    letter, maximum, minimum, password = parse_password(param)
    count = password.count(letter)
    return int(minimum) <= count <= int(maximum)


def parse_password(param):
    rule, password = param.split(': ')
    min_max_rule, letter = rule.split(' ')
    minimum, maximum = min_max_rule.split('-')
    return letter, maximum, minimum, password


def get_data_from_file(filename):
    with open(filename) as f:
        data = f.read()
    return data


def valid_password_count(passwords, password_checker):
    return sum([password_checker(x) for x in passwords])


def main(filename, password_checker):
    data = get_data_from_file(filename)
    passwords = read_password(data)
    print(valid_password_count(passwords, password_checker))


def check_password_occurence_position(param):
    letter, maximum, minimum, password = parse_password(param)
    in_mimimum = password[int(minimum) - 1] == letter
    in_maximum = password[int(maximum) - 1] == letter
    return True if in_maximum ^ in_mimimum else False

if __name__ == '__main__':
    main('day_2.txt', check_password_nb_occurence)
    main('day_2.txt', check_password_occurence_position)