def reverse_number(n):
    rev=0 
    while n>0:
        rem=n%10
        n=n//10
        rev=rev*10 + rem 
     return rev 
    