from pandas import read_excel
from os import getcwd

path = getcwd()
path_new = path.replace("\\","/")

asin_path = path_new + "/TotalSalesAsinList.tsv"
configfile_path = path_new + "/EQ convert Config File.xlsx"

bool_df = read_excel(configfile_path, sheet_name="Sheet1", index_col="Parameter")
bool_df.drop("Notes:", axis=1, inplace =True)
bool_df["bool"] = bool_df.Value == "y"


wm_bool = bool_df["bool"]["Weight (Metric)"]
wi_bool = bool_df["bool"]["Weight (Imperial)"]
v_bool = bool_df["bool"]["Volume"]
mi_bool = bool_df["bool"]["Multiple Items"]