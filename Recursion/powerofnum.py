def power(base, exp):
    assert exp >= 0 and int(exp) == exp, 'The exponentmust be positive integer'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * (base * exp-1)

base = int(input('Enter the base: '))
exp = int(input('Enter the exponent: '))

print(power(base,exp))
