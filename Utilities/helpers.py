import random
import string


class GenerateRandomString:
    @staticmethod
    def generate_random_str_letters(length: int):
        s = ''.join(random.choices(string.ascii_letters, k=length))
        return s

    @staticmethod
    def generate_random_str_letters_and_digits(length: int):
        digit = random.choice(string.digits)
        s = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        result = list(s + digit)
        random.shuffle(result)
        return ''.join(result)
