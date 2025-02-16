wordlist = ['password', 'john', 'qwerty', 'admin']

for word in wordlist:
    counter = 0
    while counter < 100:
        print(f'{word}{counter}')
        counter = counter + 1
