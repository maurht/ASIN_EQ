def num_count(desc):
    desc_s = desc.split()
    n=0

    for word in desc_s:
        try:
            if float(word) < 3000:
                n=n+1
        except:
            pass
    
    return n