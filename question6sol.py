def min_list(list):
    min=list[0]
    secMin=list[0]
    for i in list:
        if(i<min):
            min=i
    for i in list:
         if(i<secMin and i>min):
            secMin=i       

    return secMin    


list=[1,2,-8,-2,-10]
print("Second Minimum of list is: ",min_list(list))