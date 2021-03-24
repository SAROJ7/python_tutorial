import random

value = random.randint(0,1)
print(value)


greetings = ['Hello', 'Hi', 'Namaste', 'Hola', 'Howdy']

value = random.choice(greetings)
print(f'{value}, Saroj!')

colors = ['Red', ' Black', 'Yellow', 'White']

results = random.choices(colors, weights= [18, 15, 1, 4 ], k= 10)

print(results)

deck = list(range(1, 53))
hand = random.sample(deck, k=5)
print(hand)