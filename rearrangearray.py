#Create a function that takes a list lst of numbers and moves all zeros to the end, preserving the order of the other elements.

def move_zeros(lst):
    newlst=[]
    for i in lst:
        if i!=0:
            newlst.append(i)
    for j in lst:
        if j==0:
            newlst.append(j)
    return newlst
