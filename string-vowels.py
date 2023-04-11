import string


num = 0 
vowel_str = input('Enter a string: ')

for ch in vowel_str: 
    if ch in vowel_str: 
        if ch in "aeiou":
            num = num + 1

print('Your string has', num, 'vowels')
