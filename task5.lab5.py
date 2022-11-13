from random import sample
import string

def get_random_password(n=8) -> str:
    alphavit = string.digits + string.ascii_letters
    alphavit_list = [letter for letter in alphavit]
    passworld = sample(alphavit_list, n)
    return "".join(passworld)

print(get_random_password())
