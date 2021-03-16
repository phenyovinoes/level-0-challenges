def vowel(string):
    vowels = 'uoiea'
    for char in vowels:
        if char in string:
            print(char, end=',')
print("Vowels:", end=' ')


vowel()
