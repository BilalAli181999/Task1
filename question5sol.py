def min_list(list):
    min=list[0]
    for i in list:
        if(i<min):
            min=i
    return min     


list=[1,2,-8,-2,-90]
print("Minimum of list is: ",min_list(list))