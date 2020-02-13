from exerciseFeb12 import *
import random

jedi1 = Jedi("Lior")
jedi2 = Jedi("Shlomo")
jedi3 = Jedi("Eran")

sith1 = Sith("Sarah")
sith2 = Sith("Eli")
sith3 = Sith("Jason")

live_jedi = [jedi1, jedi2, jedi3]
live_sith = [sith1, sith2, sith3]

counter = 0
while live_sith and counter < 100:
    counter += 1
    jedi = random.choice(live_jedi)
    sith = random.choice(live_sith)

    if sith.fight(jedi):
        sith.train()
        jedi.train()
    else:
        live_sith.remove(sith)
        jedi.train()
    print(counter)
    # if counter > 100:
    #     break

if counter >= 100:
    print(f'Siths have taken over the Galaxy. Goodbye.')
else:
    print(f'Jedis have won in {counter} fights')

