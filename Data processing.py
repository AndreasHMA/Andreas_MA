# Imports
import pandas as pd
import os
from geopy.geocoders import Nominatim

# Reading the Excel-file into a Dataframe.
df = pd.read_excel("Please enter filename.xlsx")

# Combining the columns "geo.country" and "geo.name"
# into a new column called "full_address".
df["full_address"] = df["geo.country"] + "," + df["geo.name"]

# Initialising GeoPy with a timeout of 10 seconds between the calls
# and a user_agent for limiting the number of requests.
geolocator = Nominatim(timeout=10, user_agent="myGeolocator_MA")

# Calling the longitude and latitudes values with geolocator
# and writing them into the Dataframe into two new columns.
# If the values aren´t detectable it will write "NF" for "Not found" instead.
df["lat"] = df["full_address"].apply(lambda x: geolocator.geocode(x).latitude if geolocator.geocode(x) != None else "NF")
df["long"] = df["full_address"].apply(lambda x: geolocator.geocode(x).longitude if geolocator.geocode(x) != None else "NF")

# Counting the unique values for each unique location in
# the "geo.full_name" column and writing the result into a new Dataframe
# with the column called count.
df_new = df["geo.full_name"].value_counts(sort=False).to_frame("count")

# Dropping the duplicates of the column "geo.full_name"
# and merging the Dataframes df_new and df into one Dataframe.
df = df.drop_duplicates(subset=["geo.full_name"])
df_merged = pd.concat([df, df_new], ignore_index=False)

# Saving the merged Dataframe into an Excel-file.
new_file = os.path.join("Please enter filename.xlsx")
writer = pd.ExcelWriter(new_file)
df_merged.to_excel(writer, sheet_name="Please enter filename.xlsx", index=False)
writer.close()
