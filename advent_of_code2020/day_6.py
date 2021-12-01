def questions_group_anyone_answered_yes(data):
    return(len(set(data.replace('\n', ''))))


def sum_of_count(data, conditiion):
    return sum([conditiion(_) for _ in data.split('\n\n')])


def main(file, condition):
    with open(file, 'r') as f:
        data = f.read()
    return sum_of_count(data, condition)


def questions_group_everyone_answered_yes(data):
    data_by_person = data.split('\n')
    number_of_person = len(data_by_person)

    nb_of_answer_by_question = {}
    for answers_by_person in data_by_person:
        for answer_by_person in answers_by_person:
            if answer_by_person not in nb_of_answer_by_question:
                nb_of_answer_by_question[answer_by_person] = 0
            nb_of_answer_by_question[answer_by_person] += 1
    return sum([1 if nb_of_answer_by_question[_] == number_of_person else 0 for _ in nb_of_answer_by_question])


if __name__ == '__main__':
    print(main('day_6.txt', questions_group_anyone_answered_yes))
    print(main('day_6.txt', questions_group_everyone_answered_yes))


