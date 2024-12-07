password = input('Введите пароль: ')


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_letters(password):
    return any(letter.isalpha() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isdigit()
               and not letter.isalpha() for letter in password)


def main():
    functions = [
        is_very_long(password),
        has_digit(password),
        has_letters(password),
        has_upper_letters(password),
        has_lower_letters(password),
        has_symbols(password)
    ]

    score = 0

    for function in functions:
        if function:
            score += 2

    print('Рейтинг пароля: ', score)


if __name__ == '__main__':
    main()
