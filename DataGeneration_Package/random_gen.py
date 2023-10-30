import random

def generate_num(probability = 0.96):
    return 1 if random.random() < probability else 0