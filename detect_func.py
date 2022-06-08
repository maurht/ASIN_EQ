from numpy import nan

def detect(desc_procesed, keywords, n, integer):
    #desc_procesed: already procesed description or item name
    #keywords: list of keywords to find
    #n: number of words that the keyword and the number are apart (most probably +1 (right) or -1 (left))
    #integer: If true, the return value is suposed to be an integer

    desc_p_s = desc_procesed.split()  #Separate description at spaces
    
    aux_kw = " " + ". ".join(keywords.split()) + "."  #duplicate keyword list but with a point at the end of keywords
    total_kw = keywords + aux_kw #oz ounce -> oz oz. ounce ounce.

    kw_l = total_kw.lower().split()  #Separate keyword list at spaces

    #Steps
    #1: Go through every word in split description 
    #2: check if the word is in keyword list, let the word n steps from it be x 
    #3: Check if x is really a number. We have two cases:
    #3.1: x is suposed to be an integer (int=True), check by: If x is indeed an integer then 
    #    int(x) = float(x) -> int(x) - float(x) = 0. If the condition holds return x, if not return nothing (nan)
    #3.2: x is not suposed to be an integer, return float(x)
    #4: If x is reaaly not a number, do nothing
    #5: If the cycle finishes and there's no return value, return nothing (nan)


    for word in range(len(desc_p_s)):   #1
        if desc_p_s[word] in kw_l:      #2
            x = desc_p_s[word+n] 

            if (x.replace(".","")).isdigit():       #3
                if integer:                         #3.1
                    if int(x) - float(x) == 0: 
                        return float(x)
                    else:
                        return nan
                    
                else:                               #3.2
                    return float(x)
            else:                                   #4
                pass
        
    return nan      #5