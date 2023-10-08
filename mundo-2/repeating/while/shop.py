print('-'*20)
print('Shop')
print('-'*20)

sum = count = lowest_value = 0
lowest_value_name = ''

while True:
    product_name = str(input("Product name: "))
    price = float(input("Price: R$"))

    sum += price
    count += 1
    
    if count == 1:
        lowest_value = price

    if price < lowest_value:
        lowest_value = price
        lowest_value_name = product_name
    
    continue_or_not = str(input("Do want continue? [Y/N]")).upper().strip()

    while continue_or_not not in 'YN':
        continue_or_not = str(input("Do want continue? [Y/N]")).upper().strip()
    if continue_or_not == 'N':
        break

print(f"Sum total: R${sum}")
print(f"Lowest value: R${lowest_value} {lowest_value_name}")
