import random
def generate_random_string():
    return ''.join(str(random.randint(0, 9)) for _ in range(12))