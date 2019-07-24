

def result(n):
    sum=0
    for i in range(3):
        sum+=n**(i+1)
    return sum    


n=int(input("Enter a number: "))
print(result(n))