def isVowel(ch):
    vowels=['a','e','i','o','u']
    if ch in vowels:
        print(ch," is a Vowel")
    else:
        print(ch," is a consonant") 


ch=input("Enter a chachter?")
isVowel(ch)