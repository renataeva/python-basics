#!/usr/bin/env python

import pyttsx3
import random
import time

engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

words = open('words.txt').readlines()

N = 20
print(f"Total {len(words)} words.")
delay_opt = input("Auto-delay between words N/[Y]")
if delay_opt == "Y":
    delay_t = 10
    r = input(f"  Delay time. Default {delay_t} sec.")
    if r != "":
        delay_t = int(r)
else:
    delay_t = 0
opt = input(f"""1. {N} words shuffled
2. ALL alphabetical order
3. ALL shuffled
4. N shufled\n""")
if opt == "":
    opt = "1"

if opt == "1":
    random.shuffle(words)
elif opt == "2":
    words.sort()
    N = len(words)
elif opt == "3":
    random.shuffle(words)
    N = len(words)
elif opt.startswith("4"):
    N = int(input("Number of words: "))
    random.shuffle(words)
else:
    print(f"Wrong input provided: {opt}")
    exit(1)

for i in range(N):
    w = words[i]
    engine.say(w)
    engine.runAndWait()
    if delay_t > 0:
        print(f"{i+1} ", end='')
        time.sleep(delay_t)
    else:
        print(f"{i+1}{input('')} ", end='')
print()
for i in range(N):
    print(f"{i + 1} {words[i]}", end='')

engine.stop()
