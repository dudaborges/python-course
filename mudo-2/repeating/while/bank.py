fifties_banknotes = 0
ten_banknotes = 0
one_banknotes = 0

print('=' * 20)
print(f'{'BANK CEV':^20}')
print('=' * 20)

value = float(input('what amount do you want to withdraw?'))

while True:
    if value / 50 > 1:
        value -= 50
        fifties_banknotes += 1
    else:
        break

while True:
    if value / 10 > 1:
        value -= 10
        ten_banknotes += 1
    else:
        break

while True:
    one_banknotes += 1
    if value / 1 > 1:
        value -= 1
    else:
        break

print(f'Fifties backnotes total: {fifties_banknotes}')
print(f'Ten backnotes total: {ten_banknotes}')
print(f'One backnotes total: {one_banknotes}')