from detect_func import detect
from special_pack_funcs import n_packsof_m, parenthesis_pack, packsof_n, n_by_m
from numpy import isnan, nan


def feats(df, wm_bool, wi_bool, v_bool, mi_bool):
    if wm_bool:
        df["Weight_kilo"] = df["desc_p"].apply(lambda x: detect(x,"kg kilo kgs kilos",-1, False))
        df["Weight_gram"] = df["desc_p"].apply(lambda x: detect(x,"gr grs grams gram",-1, False))

        #df["Weight_metric [Kg]"] = df["Weight_metric_kilo"] + asin_list["Weight_metric_gram"] / 1000


    if wi_bool:
        df["Weight_ounce"] = df["desc_p"].apply(lambda x: detect(x,"ounce ounces oz",-1, False))
        df["Weight_pound"] = df["desc_p"].apply(lambda x: detect(x,"pound pounds lb lbs",-1, False))

        #df["Weight_imperial [Lb]"] = df["Weight_imperial_ounce"] + asin_list["Weight_imperial_pound"] / 16


    if v_bool:
        df["Volume_floz"] = df["desc_p"].apply(lambda x: detect(x,"fl",-1, False))
        df["Volume_L"] = df["desc_p"].apply(lambda x: detect(x,"L liter liters",-1, False))
        df["Volume_ml"] = df["desc_p"].apply(lambda x: detect(x,"ml",-1, False))

        #df["Volume [V]"] = 0.0295735 * df["Volume_floz"] + asin_list["Volume_L"] + asin_list["Volume_ml"] /1000


    if mi_bool:
        df["pack_aux_1"] = df["desc_p"].apply(lambda x: packsof_n(x))
        df["pack_aux_2"] = df["desc_p"].apply(lambda x: detect(x,"pack",-1, True))
        df["pack_aux_3"] = df["item_name"].apply(lambda x: parenthesis_pack(x)) 
        df["pack_aux_4"] = df["desc_p"].apply(lambda x: n_packsof_m(x))
        df["pack_aux_5"] = df["desc_p"].apply(lambda x: n_by_m(x))

        df["pack"] = nan
        df["pack_2"] = nan
        df["pack_3"] = nan

        #dump mult_aux_i into a single column
        #Take care of rows that detected more than one pattern. Optional as this is rare

        for row in range(len(df)):
            for i in range(1,6):
                n = 0
                pack_i = "pack_aux_" + str(i)
                if not isnan(df[pack_i].iloc[row]) and n == 0:
                    df["pack"].iloc[row] = df[pack_i].iloc[row]
                    n = 1
                elif not isnan(df[pack_i].iloc[row]) and n == 1:
                    df["pack_2"].iloc[row] = df[pack_i].iloc[row]
                    n=2
                elif not isnan(df[pack_i].iloc[row]) and n == 2:
                    df["pack_3"].iloc[row] = df[pack_i].iloc[row]

        df.drop(["pack_aux_1","pack_aux_2","pack_aux_3","pack_aux_4","pack_aux_5",], axis=1, inplace=True) #drop aux columns

        if df["pack_2"].isnull().sum() == len(df):
            df.drop("pack_2", axis=1, inplace=True)

        if df["pack_3"].isnull().sum() == len(df):
            df.drop("pack_3", axis=1, inplace=True)


    return df