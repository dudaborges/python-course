gender = input('Enter your gender (F/M): ').lower().strip()[0]
# while gender != 'f' and gender != 'm':
#     print('[ERROR] Invalid value')
#     newGender = input('Please, enter your gender again (F/M): ').lower().strip()[0]
#     gender = newGender
while gender not in 'FfMm':
    print('[ERROR] Invalid value')
    gender = input('Please, enter your gender again (F/M): ').lower().split()[0]
print(f'Gender {gender} successfully registered')



