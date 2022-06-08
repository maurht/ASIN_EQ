from numpy import isnan, nan

def simultaneous_non_nan(dataframe, col_list, feat_bool):
    

    if feat_bool:                               #If the feature exist
        for i in range(len(dataframe)):         #cycle through every row
            
            counter = 0                         #non nan column counter
            for c in col_list:                  #cycle through col_list
                counter = counter + int(not isnan(dataframe[c].loc[i]))     #add one to counter if at i row and 
                                                                            #at c column there is a non nan value

            if counter > 1:                                 #if the counter is bigger than one, issue warning
                dataframe["warning"].loc[i] = "x"

    return dataframe



def warnings(dataframe, weight_metric, weight_imperial, volume):

    dataframe["warning"] = nan      #create warning column

    #if the number count is 0, then there is no way that any usefull information is recovered. Issue a warning

    dataframe["warning"].fillna(dataframe["num_count"].apply(lambda nc: "x" if nc == 0 else nan), inplace=True)

    #if the number count is different fron the total number of units captured by the program raise a warning
    #it's important to take only in count columns with units, so we create a copy of the dataframe with only the 
    #unit columns

    asin_list_aux = dataframe.drop(["ASIN","item_name", "desc_p","num_count", "warning"], axis=1)

    
    for i in range(len(dataframe)):
        count_non_nan = 0
        for col in asin_list_aux.columns:
            if not isnan(asin_list_aux[col].loc[i]):
                count_non_nan = count_non_nan + 1

        if dataframe["num_count"].loc[i] != count_non_nan:
            dataframe["warning"].loc[i] = "x"

    #issue a warning if for multiple pack patterns detected. Highly unlikely and is a little extra 
    #logic very similar to simultaneous_non_nan function but modified to cycle through all pack columns,
    #that is, if more than one exists which is the very unlikely part

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

    #Same as above but for unit columns. The simultaneous_non_nan function defined above is used here
    #For a group of units (col_list) [feat_bool is checked here to see if the columns even exist]
    # it'll check for non nan values. If it finds more than one non value it'll issue a warning
    
    dataframe = simultaneous_non_nan(dataframe, col_list=["Weight_gram", "Weight_kilo"], feat_bool= weight_metric)

    dataframe = simultaneous_non_nan(dataframe, ["Weight_ounce", "Weight_pound"], weight_imperial)

    dataframe = simultaneous_non_nan(dataframe, ["Volume_floz", "Volume_L", "Volume_ml"], volume)
    

    return dataframe