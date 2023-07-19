def factorial(num):
    i=1
    if num==0 :
        return 1
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(int(input())))
