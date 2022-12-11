import random
import string
def get_random_password() -> str:
    string_ = string.digits + string.ascii_letters
    pass_ = "".join(random.sample(string_,8))
    return pass_

print(get_random_password())
