word = input('Word: ')
word = word.lower()
word = word.replace(' ','')
check = word.find(word[::-1])==0
if check:
    print('Palindrome')
else:
    print('Not a palindrome')