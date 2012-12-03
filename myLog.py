def myLog(x,b):
    i= 0
    answer = 0
    while True:
        #calculate pow(b,i)
        
        answer = pow(b,i)
        
        
        if answer > x:
            i = i-1
            break
        elif answer == x:
            break
        else:
            i = i+1

        
        
        
    return i
