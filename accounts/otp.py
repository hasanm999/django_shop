import random


def generate_otp():

    otp = random.randint(
        100000,
        999999
    )

    print(f'OTP Code: {otp}')

    return otp