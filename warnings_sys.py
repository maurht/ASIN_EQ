from numpy import isnan, nan

def simultaneous_non_nan(dataframe, col_list, feat_bool):
    if feat_bool:
        for i in range(len(dataframe)):
            
            counter = 0
            for c in col_list:
                counter = counter + int(not isnan(dataframe[c].loc[i]))

            if counter > 1:
                dataframe["warning"].loc[i] = "x"

    return dataframe

#IMPORT FEAT BOOLS TO GET RID OF TRY's


def warnings(dataframe, weight_metric, weight_imperial, volume):

    dataframe["warning"] = nan

    dataframe["warning"].fillna(dataframe["num_count"].apply(lambda nc: "x" if nc == 0 else nan), inplace=True)

    asin_list_aux = dataframe.drop(["ASIN","item_name", "desc_p","num_count", "warning"], axis=1)


    for i in range(len(dataframe)):
        count_non_nan = 0
        for col in asin_list_aux.columns:
            if not isnan(asin_list_aux[col].loc[i]):
                count_non_nan = count_non_nan + 1

        if dataframe["num_count"].loc[i] != count_non_nan:
            dataframe["warning"].loc[i] = "x"


    col_list = dataframe.columns
    total_mult_cols = 0

    for c_name in col_list:
        if len(c_name.replace("pack","")) != len(c_name):
            total_mult_cols = total_mult_cols + 1

    if total_mult_cols > 1:
        for i in range(len(dataframe)):
            counter = 0

            for i in range(total_mult_cols):
                col_i = "pack_aux_" + str(i)
                counter = counter + int(not isnan(dataframe[col_i].loc[i]))
            if counter > 1:
                dataframe["warning"].loc[i] = "x"

 
    dataframe = simultaneous_non_nan(dataframe, ["Weight_gram", "Weight_kilo"], weight_metric)

    dataframe = simultaneous_non_nan(dataframe, ["Weight_ounce", "Weight_pound"], weight_imperial)

    dataframe = simultaneous_non_nan(dataframe, ["Volume_floz", "Volume_L", "Volume_ml"], volume)
    

    return dataframe