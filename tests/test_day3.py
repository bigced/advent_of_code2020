from unittest import mock

from advent_of_code2020.day_3 import get_number_of_trees_from_data, extract_lines_from_data, \
    traverse_file_mountain_data, main


def test_count_number_of_trees():
    data = """..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"""
    nb_of_trees = get_number_of_trees_from_data(data, right=3, down=1)
    assert nb_of_trees == 7


def test_count_number_of_trees_repeat():
    data="""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    nb_of_trees = get_number_of_trees_from_data(data, right=3, down=1)
    assert nb_of_trees == 7


def test_extract_lines_from_data():
    data = """..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"""
    lines = extract_lines_from_data(data)
    assert len(lines) == 11
    assert lines[-1] == ".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"


@mock.patch('builtins.print')
def test_traverse_file_mountain_data(mocked_print):
    file_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    mock_open = mock.mock_open(read_data=file_data)
    with mock.patch('builtins.open', mock_open):
        assert traverse_file_mountain_data('day_3.txt', right=1, down=1) == 2
        assert traverse_file_mountain_data('day_3.txt', right=3, down=1) == 7
        assert traverse_file_mountain_data('day_3.txt', right=5, down=1) == 3
        assert traverse_file_mountain_data('day_3.txt', right=7, down=1) == 4
        assert traverse_file_mountain_data('day_3.txt', right=1, down=2) == 2



def test_main():
    file_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    mock_open = mock.mock_open(read_data=file_data)
    with mock.patch('builtins.open', mock_open):
        assert 336 == main('file.txt', [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])