# Imports
import pandas as pd
import os

# Reading the CSV-file into Dataframe.
# Dropping the duplicates in the columns
# "text" and keeping the first instance of the duplicate.
df = pd.read_csv("Please enter filename.csv")
df_drop = df.drop_duplicates(subset="text", keep="first")

# Saving the Dataframe as Excel-file in the current Directory.
new_file = os.path.join("Please enter filename.xlsx")
writer = pd.ExcelWriter(new_file)
df_drop.to_excel(writer, sheet_name="Please enter filename.xlsx", index=False)
writer.close()
