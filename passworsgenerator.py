# Generate Secure Passwords:
# fixed length, At least 12 characters long is recommended, 8 at the minimum. The
# combination of both upper- and lower-case letters, numbers, and symbols. Random enough that
# they do not contain any predictable sequence

# code-
import random
def generate():
    n = random.randint(8,12)
    l = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
    return ''.join(random.choices(l,k=n))
print("Generated password is: ",generate())
