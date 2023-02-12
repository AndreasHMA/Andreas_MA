# Imports
import pandas as pd
import os

# Reading the Excel-file into a Dataframe.
# Filtering the columns text after certain keywords
# and writing the matching rows into a new Dataframe.
# Saving Dataframe into an Excel-file.
df = pd.read_excel("Please enter filename.xlsx")
new_df = df[df["text"].str.contains("Please enter keyword")]

# Saving the CSV as an Excel-file in your current Directory.
new_file = os.path.join("Please enter filename.xlsx")
writer = pd.ExcelWriter(new_file)
new_df.to_excel(writer, sheet_name="Please enter filename.xlsx", index=False)
writer.close()
