from numpy import nan

#each of this functions look for diferent structures in the description string
#an example is added for easier understanding


def n_packsof_m(desc):
    #Purina Beneful Wet Dog Food Variety Pack - (2 Packs of 27) 3 oz. Cans
    #                                            |           | 2*27 = Pack number wanted

    desc_s = desc.split()

    try:
        for index, word in enumerate(desc_s):
            if (word == "packs" or word == "pack") and desc_s[index+1] == "of":
                try:
                    m = float(desc_s[index+2])
                    n = float(desc_s[index-1])
                    return m*n
                except:
                    return nan
    except:
        pass
    
    return nan


def n_by_m(desc):
    #Purina Fancy Feast Roasted Turkey Food, 24 By 3 Oz.
    #                                         |  Pack number wanted
    desc_s = desc.split()

    try:
        for index, word in enumerate(desc_s):
            if word == "by":
                try:
                    m = float(desc_s[index+1])
                    n = float(desc_s[index-1])
                    return n
                except:
                    return nan
    except:
        pass
    
    return nan


def packsof_n(desc):
    #Purina Busy Rollhide Beef, Small/Medium 4 Ounce, 3 ct (Pack of 1)
    #                                                               | Pack number wanted

    desc_s = desc.split()

    try:
        for index, word in enumerate(desc_s):
            if word == "pack" and desc_s[index+1] == "of":
                try:
                    float(desc_s[index-1])
                    pass
                except:
                    try:
                        return float(desc_s[index+2])
                    except:
                        pass
    except:
        pass
    
    return nan


def parenthesis_pack(desc):
    #Purina Beggin' Strips Real Meat Dog Treats, Bacon & Beef Flavors - (6) 6 oz. Pouches
    #                                                                    | Pack number wanted

    desc_fix = ("".join(desc.lower().split())).replace(")","(")
    desc_fix_s = desc_fix.split(sep="(")

    for x in desc_fix_s:
        try:
            pack = float(x)
            if pack < 1000:
                return pack
            else:
                pass 
            return 
        except:
            pass

    return nan
