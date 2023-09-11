# bcrypt (Password Hashing):

# Bcrypt is a specialized hash function designed for securely hashing passwords.
# It includes salting and multiple iterations to make brute-force attacks more difficult.
# You can use the bcrypt library in Python for bcrypt hashing:

import bcrypt

import bcrypt

def PassHash(password):
    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    print(hashed_password.decode('utf-8'))

PassHash('password')
