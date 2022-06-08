from pandas import read_excel
from os import getcwd

#the program will asume that the config file is in the same folder. Steps:
#1. Get the path the program is on and change slashes \ -> /
#2. from path get the path of TotalSalesAsinList and config file
#3. Read config file 
#4. Create column bool = True if Value column is "y", False in any other case
#5. Extract features user wants

#1
path = getcwd()                                                         
path_new = path.replace("\\","/")

#2
asin_path = path_new + "/TotalSalesAsinList.tsv"
configfile_path = path_new + "/EQ convert Config File.xlsx"

#3
bool_df = read_excel(configfile_path, sheet_name="Sheet1", index_col="Parameter")
bool_df.drop("Notes:", axis=1, inplace =True)

#4
bool_df["bool"] = bool_df.Value == "y"

#5
wm_bool = bool_df["bool"]["Weight (Metric)"]
wi_bool = bool_df["bool"]["Weight (Imperial)"]
v_bool = bool_df["bool"]["Volume"]
mi_bool = bool_df["bool"]["Multiple Items"]

#the variables are then extracted from here by master.py file