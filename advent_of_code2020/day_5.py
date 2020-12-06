def split_col_data(min_range, max_range, boarding_pass):
    if boarding_pass[0] == 'L':
        return min_range, min_range + (max_range - min_range) // 2, boarding_pass[1:]
    return max_range - (max_range - min_range) // 2, max_range, boarding_pass[1:]


def decode_column_from_boarding_pass(boarding_pass):
    min_range = 0
    max_range = 7
    boarding_pass = boarding_pass[7:]
    while len(boarding_pass) > 0:
        min_range, max_range, boarding_pass = split_col_data(min_range, max_range, boarding_pass)
    return min_range


def split_row_data(min_range, max_range, boarding_pass):
    if boarding_pass[0] == 'F':
        return min_range, min_range + (max_range - min_range) // 2, boarding_pass[1:]
    return max_range - (max_range - min_range) // 2, max_range, boarding_pass[1:]


def decode_row_from_boarding_pass(boarding_pass):
    min_range = 0
    max_range = 127
    boarding_pass = boarding_pass[:7]
    while len(boarding_pass) > 0:
        min_range, max_range, boarding_pass = split_row_data(min_range, max_range, boarding_pass)
    return min_range


def get_seat_id(row, column):
    return row*8 + column


def main(file):
    with open(file, 'r') as f:
        data = f.read()
    seat_ids = []
    for bp in data.split('\n'):
        row = decode_row_from_boarding_pass(bp)
        column = decode_column_from_boarding_pass(bp)
        seat_ids.append(get_seat_id(row, column))
    return max(seat_ids)


def main_2(file):
    with open(file, 'r') as f:
        data = f.read()
    seat_ids = []
    for bp in data.split('\n'):
        row = decode_row_from_boarding_pass(bp)
        column = decode_column_from_boarding_pass(bp)
        seat_ids.append(get_seat_id(row, column))
    seat_ids.sort()
    i = 0
    j = 1
    max_index = len(seat_ids) - 1
    print(seat_ids)
    while j <= max_index:
        if seat_ids[j] - seat_ids[i] != 1:
            print(seat_ids[i], seat_ids[j])
        i = i + 1
        j = j + 1


if __name__ == '__main__':
    print(main('day_5.txt'))

    main_2('day_5.txt')