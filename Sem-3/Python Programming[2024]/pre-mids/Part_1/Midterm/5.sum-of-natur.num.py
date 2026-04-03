n = int(input('Enter till where to add all natural numbers : '))

if n < 0:
    print('Enter natural numbers only!')
elif n > 0:
    total = 0
    while n > 0:
        total = n + 1
        n = n - 1

    print('The Sum value is  :  ', total)
else:
    print('Enter numbers only!')


