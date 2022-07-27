import bcrypt


def hash(string):
    return bcrypt.hashpw(string.encode(), bcrypt.gensalt()).decode()


def check(string, hashed_string):
    return bcrypt.checkpw(string.encode(), hashed_string.encode())


if __name__ == '__main__':
    password = '1234'
    hashed_string_password = hash(password)
    print(hashed_string_password)
    is_the_same = check(password, hashed_string_password)
    print(is_the_same)

# password = hash('123456')
# print(password)
