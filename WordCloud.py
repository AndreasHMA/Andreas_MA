# Imports
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import pandas as pd

# Data preparation
# Reading the two Excel-files in your Directory with the negative and positive words into two separate Dataframes.
df_positive_concatenated = pd.read_excel("Please enter filename.xlsx")
df_negative_concatenated = pd.read_excel("Please enter filename.xlsx")

# Joining the tokens in the columns "positive token" and "negative token" to a string.
positive_pol_str = ','.join(str(x) for x in df_positive_concatenated["positive token"])
negative_pol_str = ','.join(str(x) for x in df_negative_concatenated["negative token"])

# Creating the Word Clouds
# Creating and saving the positive Word Cloud with the string of positive tokens.
# Defining the characteristics: background color, max words,
# font, font size, collocations, stopwords, size and title.
positive_cloud = WordCloud(background_color="white",
                           max_words=50,
                           font_path="arial.ttf",
                           max_font_size=1000,
                           collocations=False,
                           stopwords=set()).generate(positive_pol_str)
plt.figure(figsize=(19, 10))
plt.axis("off")
plt.title("positive WordCloud", fontsize=30)
plt.imshow(positive_cloud)
plt.savefig("positive WordCloud.jpg")
plt.show()

# Creating and saving the negative Word Cloud with the string of negative tokens.
# Defining the characteristics: background color, max words,
# font, font size, collocations and stopwords, size and title.
negative_cloud = WordCloud(background_color="white",
                           max_words=50,
                           font_path="arial.ttf",
                           max_font_size=1000,
                           collocations=False,
                           stopwords=set()).generate(negative_pol_str)
plt.figure(figsize=(19, 10))
plt.axis("off")
plt.title("negative WordCloud", fontsize=30)
plt.imshow(negative_cloud)
plt.savefig("negative WordCloud.jpg")
plt.show()
