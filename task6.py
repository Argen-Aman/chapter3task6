from decimal import Decimal

your_weight = float(input('Your weight: '))

x = Decimal(your_weight*0.165)
your_moon_weight = round(x,2)

print(f'If you were on the moon now, your weight will be {your_moon_weight} kg.\n')
print('But next 15 years . . .')

def talking_to_the_moon (your_weight):
    i = 1
    each_year = 0.165
    new_weight = float(your_moon_weight)
    while i <= 15:
        new_weight = new_weight + each_year
        new_weight_rounded = round(new_weight,2)
        print(f'Till the end of {i}-year your weight will be {new_weight_rounded} kg.')
        i += 1
        your_weight += 1
talking_to_the_moon (your_weight)
