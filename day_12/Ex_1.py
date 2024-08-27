import random
import string

characters = string.ascii_letters + string.digits

random_choices = [random.choice(characters) for i in range(6)]

print(random_choices)
