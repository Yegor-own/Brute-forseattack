import random


class PasswordGenerator:
    letters_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits_alphabet = '0123456789'
    specsymbols_alphabet = '.,/?!@#$%^&*():;\'"|\\'

    def __init__(self, length=16, use_letters=True,
                 use_digits=True, use_specsymbols=False):
        self.length = length
        self.use_letters = use_letters
        self.use_digits = use_digits
        self.use_specsymbols = use_specsymbols
        print('Init:', length, use_letters, use_digits, use_specsymbols)

    def generate_password(self):
        alphabet = ''
        if self.use_letters:
            alphabet += self.letters_alphabet
        if self.use_digits:
            alphabet += self.digits_alphabet
        if self.use_specsymbols:
            alphabet += self.specsymbols_alphabet
        if not alphabet:
            print('Empty alphabet')
            return

        password = ''
        for i in range(self.length):
            password += random.choice(alphabet)
        return password
