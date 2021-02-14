import random

mood_perfect = ['отличн', 'прекрасн']
mood_good = ['хорош', 'нормальн']
mood_bad = ['плох', 'ужасн']
moods = {'bad': mood_bad,
         'good': mood_good,
         'perfect': mood_perfect}

resp_perfect = ['Великолепно!', 'Супер!']
resp_good = ['Я очень рад.', 'Отлично.']
resp_bad = ['Не унывай.', 'М-да...']
resp_default = ['Извини.', 'Не понимаю.']
resps = {'bad': resp_bad,
         'good': resp_good,
         'perfect': resp_perfect}

print('Привет! Как дела?')
while True:
    ans = input().lower()

    done = False
    for name, mood in moods.items():
        for w in mood:
            if w in ans:
                print(random.choice(resps[name]))
                done = True
                break
        if done:
            break

    if not done:
        print(random.choice(resp_default))
