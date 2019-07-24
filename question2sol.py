def length(str):
    letters=0
    digits=0
    for i in str:
        if((i>='a' and i<='z') or (i>='Z' and i<='Z')):
            letters+=1
        if (i>='0' and i<='9'):
            digits+=1
    return letters,digits


str=input("Enter a string?")
let=0
dig=0
let,dig=length(str)
print("No of Digits:",dig)
print("No of Letters:",let)