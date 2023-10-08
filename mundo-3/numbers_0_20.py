NUMBERS_NAME = (
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
    'twenty',
)


def validate_number(number: int) -> int:
    """
    Checks if the number is between the range 0 to 20

    Examples:
        >>> validate_number(20)
        20
    """
    while number < 0 or number > 20:
        number = int(
            input('[ERROR] Try again. You entered an invalid number\n>> ')
        )

    return number


def write_number_in_full(number: int) -> str:
    """
    Write the number in full

    Examples:
        >>> write_number_in_full(12)
        'twelve'
        >>> write_number_in_full(10)
        'ten'
        >>> write_number_in_full(5)
        'five'
    """
    number = validate_number(number)
    number_name = NUMBERS_NAME[number]

    return number_name
