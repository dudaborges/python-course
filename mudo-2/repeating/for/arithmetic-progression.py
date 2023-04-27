print('=' * 20)
print('10 TERMS OF A AP')
print('=' * 20)
term = int(input('First term: '))
reason = int(input('Reason: '))
tenth = term + (10 - 1) * reason
for a in range(term, tenth, reason):
    print(a, end=' -> ')
print('ACABOU')