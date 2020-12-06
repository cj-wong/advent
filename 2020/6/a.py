from typing import List

import config


def count_mutual_answerable_cdf(answers: List[str]) -> int:
    """Count the number of answerable customs declaration form questions.

    Unlike count_answerable_cdf(), only answers shared by all individuals
    in a group will be counted.

    Args:
        answers (List[str]): the file answers

    """
    count = 0
    group_members = 0
    group_answers = set()
    raw_group_answers = []
    for answer in answers:
        if not answer:
            for g_ans in group_answers:
                if raw_group_answers.count(g_ans) == group_members:
                    count += 1
            group_members = 0
            group_answers = set()
            raw_group_answers = []
        else:
            for ans in answer:
                group_answers.add(ans)
                raw_group_answers.append(ans)
            group_members += 1

    if group_answers:
        for g_ans in group_answers:
            if raw_group_answers.count(g_ans) == group_members:
                count += 1

    return count


def count_answerable_cdf(answers: List[str]) -> int:
    """Count the number of answerable customs declaration form questions.

    Args:
        answers (List[str]): the file answers

    """
    count = 0
    group_answers = set()
    for answer in answers:
        if not answer:
            count += len(group_answers)
            group_answers = set()
        else:
            for ans in answer:
                group_answers.add(ans)

    if group_answers:
        count += len(group_answers)

    return count


def main() -> None:
    """Process customs declaration forms."""
    # Part A
    test_answer = 3 + 3 + 3 + 1 + 1 # 11
    file = config.TestFile(test_answer)
    test = count_answerable_cdf(file.contents)
    file.test(test)

    file = config.File()
    result = count_answerable_cdf(file.contents)
    config.LOGGER.info(result)

    # Part B
    test_answer = 3 + 0 + 1 + 1 + 1 # 6
    file = config.TestFile(test_answer)
    test = count_mutual_answerable_cdf(file.contents)
    file.test(test)

    file = config.File()
    result = count_mutual_answerable_cdf(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
