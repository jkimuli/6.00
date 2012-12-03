
def helpLaceStrings(s1, s2, out):
    
    if s1 == '':
        #PLACE A LINE OF CODE HERE
        out = out.join(s2)
    if s2 == '':
        #PLACE A LINE OF CODE HERE
        out = out.join(s1)
    else:
        #PLACE A LINE OF CODE HERE
        out = out.join(s1.replace(s1[0],'')) + out.join(s2.replace(s2[0],''))
                                                       
    return helpLaceStrings(s1, s2, '')

    

    
