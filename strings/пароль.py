ABCD = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = list(range(10))

password = input('Пароль: ')

# space check
if ' ' in password:
    print('space is not allowed')
    exit(1)

# number check
num_in_pass = False
for i in nums:
    if str(i) in password:
        num_in_pass = True
        break
if not num_in_pass:
    print('must contain number')
    exit(1)

# char check
char_in_pass = False
for i in ABCD:
    if str(i) in password:
        char_in_pass = True
        break
if not char_in_pass:
    print('must contain letter')
    exit(1)

print('good password')
exit(0)