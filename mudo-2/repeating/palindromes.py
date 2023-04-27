phrase = input('Digite uma frase: ').strip().upper()
words = phrase.split()
together = ''.join(words)
# inverse = ''
# for letter in range(len(together) - 1, -1, -1):
#     inverse = inverse + together[letter]
inverse = together[::-1]
# pega do início ao fim
print(inverse)
if together == inverse:
    print('This phrase is a palindrome')
else:
    print('This phrase is not a palindrome')