import itertools
import string


def guess_password(real_password):
    if real_password in common_passwords:
        return f"Password is a common password: {real_password}"

    chars = string.ascii_lowercase + string.digits
    attempts = 0
    if len(real_password) < 3:
        return "Password is too short"
    for password_length in range(2, 10):
        for guess in itertools.product(chars, repeat=password_length):
            # .product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
            guess = ''.join(guess)
            if guess == real_password:
                return f"password is {guess} found in {attempts} guesses"
            attempts += 1
            # print(f"Guess #{attempts}: {guess}")
    return f"Password not found after {attempts}"


if __name__ == '__main__':
    common_passwords = [
        '123456', '1234567', '12345678', '123456789', 'qwerty', 'password',  'iloveyou', '111111',
        'abc123', '1q2w3e4r', 'admin', 'qwertyuiop', '654321', '555555', 'lovely', 'password1', ]
    print(guess_password('a12345'))
