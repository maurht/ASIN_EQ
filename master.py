from pandas import read_csv
from process_desc_func import process_desc
from num_count_func import num_count
from warnings_sys import warnings
from create_feats import feats

###General process###
#1 Get path to TotalSalesAsinList and wanted features, read file
#2 Apply process description function and number counter function
#3 Apply features
#4 Set warnings and links if needed. Drop unnecesary columns 
#5 Save file

##### 1 #####

import config_file_input

asin_path = config_file_input.asin_path
wi_bool = config_file_input.wi_bool
wm_bool = config_file_input.wm_bool
v_bool = config_file_input.v_bool
mi_bool = config_file_input.mi_bool


asin_list = read_csv(asin_path, sep="\t")

##### 2 #####

asin_list = asin_list[["ASIN", "Item Name"]]
asin_list.columns = ["ASIN", "item_name"]       #not actually necesary

asin_list["desc_p"] = asin_list["item_name"].apply(lambda x:  process_desc(x))
asin_list["num_count"] = asin_list["desc_p"].apply(lambda x:  num_count(x))

##### 3 #####

asin_list = feats(asin_list, wm_bool, wi_bool, v_bool, mi_bool)

##### 4 #####

asin_list = warnings(asin_list, wm_bool, wi_bool, v_bool)

asin_list["link"] = asin_list["ASIN"].apply(lambda x: "https://www.amazon.com/dp/" + x)

asin_list.drop(["desc_p", "num_count"], axis=1, inplace=True)


##### 5 #####

path_aux = "/".join(asin_path.split(sep="/")[:-1]) + "/ASIN_EQ.csv"
asin_list.to_csv(path_aux, index=False)