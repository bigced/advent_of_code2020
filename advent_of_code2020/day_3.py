from advent_of_code2020.day_1 import multiply_element


def get_number_of_trees_from_data(data, right, down):
    lines = extract_lines_from_data(data)
    return sum([1 if line[(index // down * right) % len(line)] == '#' else 0 for index, line in enumerate(lines) if index % down == 0])


def extract_lines_from_data(data):
    return data.split('\n')


def traverse_file_mountain_data(filename, right, down):
    with open(filename, 'r') as f:
        file_data = f.read()
    trees = get_number_of_trees_from_data(file_data, right, down)
    return trees


def main(filename, slopes):
    results = [traverse_file_mountain_data(filename, _[0],_[1]) for _ in slopes]
    return multiply_element(results)


if __name__ == '__main__':
    traverse_file_mountain_data('day_3.txt', right=3, down=1)
    print("multiple", main('day_3.txt', [(1, 1), (3, 1), (5,1), (7,1), (1,2)]))
