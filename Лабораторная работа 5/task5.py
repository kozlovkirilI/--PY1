from string import ascii_lowercase, ascii_uppercase, digits
from random import sample

CHARS = ascii_uppercase + ascii_lowercase + digits
default_length = 8


# TODO написать функцию генерации случайных паролей
def get_random_password(n=default_length) -> str:
    return "".join(sample(CHARS, n))


print(get_random_password())
