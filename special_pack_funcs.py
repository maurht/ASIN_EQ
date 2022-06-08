from numpy import nan

def n_packsof_m(desc):
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
        return nan


def n_by_m(desc):
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
        return nan


def packsof_n(desc):
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