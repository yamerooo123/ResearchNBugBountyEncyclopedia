# For loop exercise

#ex. 2
def list_2():
    list_2 = [4, 3, 2, 1]
    for num in list_2:
        # answer
        print(num)

#ex.3 
def list_3():
    list_3 = ['Accidental', '4daa7fe9', 'eM131Me', 'Y!.90']
    secret = []

    for x in list_3:
        secret.append(x[:2])

    print(''.join(secret))


# input test
print(list_3())