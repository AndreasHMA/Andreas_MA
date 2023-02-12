# Imports
import pandas as pd
import plotly.graph_objects as go

# Reading the Excel-file into a Dataframe.
df = pd.read_excel("Please enter filename.xlsx")

# Defining the limits, the descriptions and the colors for the Bubble Map.
limits = [(1,2500)]
df["text"] = df["geo.name"] + " Tweet_count " + (df["count"]).astype(str)
colors = ["royalblue"]

# Creating the Bubble Map
# Iterating over the limits and writing the rows into a new DataFrame.
# Setting up the Bubble Map with the new Dataframe and
# defining the characteristics: locationmode, lon, lat, text and size
# with the help of the column names of the DataFrame.
fig = go.Figure()
for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode="country names",
        lon=df_sub["long"],
        lat=df_sub["lat"],
        text=df_sub["text"],
        marker=dict(
            size=df_sub["count"]*6,
            color=colors[i],
            line_color="rgb(40,40,40)",
            line_width=0.5,
            sizemode="area"
        ),
        name="{0} - {1}".format(lim[0], lim[1])))

# Creating the layout of the Bubble Map.
# Defining characteristics: legend, title, font size, width, height and scope.
fig.update_layout(
        showlegend=False,
        title_text="Please enter title",
        title_x=0.5,
        font_size=20,
        width=1920,
        height=1080,
        geo=dict(
            scope="world",
            landcolor="rgb(217, 217, 217)",
        )
    )
fig.show()
