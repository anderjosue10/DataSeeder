import random

def random_choice(options):
    return random.choice(options)

def random_int(min_val, max_val):
    return random.randint(min_val, max_val)

def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)