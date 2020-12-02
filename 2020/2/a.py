import config
import passwords


def main() -> None:
    """Check the number of valid passwords."""
    test_answer = 2 # Number of valid test passwords
    file = config.TestFile(test_answer)
    contents = file.contents
    valid = 0
    for line in contents:
        policy, password = line.split(': ')
        p = passwords.Password(policy, password)
        if p.valid:
            valid += 1
    file.test(valid)

    file = config.File()
    contents = file.contents
    valid = 0
    for line in contents:
        policy, password = line.split(': ')
        p = passwords.Password(policy, password)
        if p.valid:
            valid += 1
    print(valid)


if __name__ == '__main__':
    main()
