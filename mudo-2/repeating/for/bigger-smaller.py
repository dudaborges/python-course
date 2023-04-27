bigger = 0
smaller = 0
for w in range(1, 6, 1):
    weight = float(input(f'Person weight {w} '))
    if w == 1:
        bigger = weight
        smaller = weight
    else:
        if weight > bigger:
            bigger = weight
        if weight < smaller:
            smaller = weight

print(f'The biggest weight is {bigger}')
print(f'The smallest weight is {smaller}')



