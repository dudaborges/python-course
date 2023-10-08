shopping = float(input('Shopping price: '))
print('''===> PAYMENT METHODS <===
[1] cash/pix (10% discount)
[2] cash card (5% discount)
[3] 2x on card
[4] 3x or more on the card (20% interest)
''')
option = int(input('Choose the option: '))
if option == 1:
    print('R$', shopping - (shopping * 0.1))
elif option == 2:
    print('R$', shopping - (shopping * 0.05))
elif option == 3:
    print('R$', shopping)
elif option == 4:
    print('R$', (shopping * 0.2) - shopping)
else:
    print('[ERROR] Enter a valid number')
