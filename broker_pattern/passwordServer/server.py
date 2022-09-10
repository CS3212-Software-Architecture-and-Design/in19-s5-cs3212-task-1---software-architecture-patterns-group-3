import random
import string


class Server:
    def create_password(self, length):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        all = lower + upper + num + symbols

        temp = random.sample(all, length)

        password = ''.join(temp)

        return password
