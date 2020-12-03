# https://repl.it/@Levashov/hack
from generator import PasswordGenerator

generator1 = PasswordGenerator(use_specsymbols=True)
print(generator1.generate_password())
print(generator1.generate_password())

generator2 = PasswordGenerator(length=10)
print(generator2.generate_password())
print(generator2.generate_password())

generator3 = PasswordGenerator(use_letters=False, use_digits=False)
print(generator3.generate_password())
print(generator3.generate_password())
