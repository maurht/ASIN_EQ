def num_count(desc):
    #counts number of numbers in description that are lower than 
    # 3000. This is to avoid counting serial numbers and such

    desc_s = desc.split()
    n=0

    for word in desc_s:
        try:
            if float(word) < 3000:
                n=n+1
        except:
            pass
    
    return n