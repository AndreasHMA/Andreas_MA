# Imports
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
import re
import os

# Reading the Excel-file into a Dataframe.
df = pd.read_excel("Please enter filename.xlsx")

# Preparing Text
# Removing URL-Links and defined characters.
# Lowercasing the Tweets in the column text.
df["text"] = df["text"].str.replace(r'https?://[^ ]+', '', regex=True).str.replace(r'@[^ ]+', '', regex=True)
df["text"] = df["text"].str.replace(r'@ [^ ]+', '', regex=True).str.replace(r'#[^ ]+', '', regex=True)
df["text"] = df["text"].str.replace(r'&amp[^ ]+', '', regex=True).str.replace(r'([A-Za-z])\1{2,}', r'\1', regex=True)
df["text"] = df["text"].apply(lambda x: " ".join(x.lower() for x in x.split()))

# Loading the pretrained
# large english Pipeline from SpaCy.
nlp = spacy.load("en_core_web_lg")

# Preparing NlP-Pipeline
# Creating and Adding the custom component
# SpacyTextBlob to the NLP-Pipeline.
nlp.add_pipe("spacytextblob")

# Creating the Output-Dataframe of the Sentiment Analysis with the columns
# "created_at", "text" and "Polarity".
df_Sent_updated_info = {"created_at": [], "text": [], "Polarity": []}
df_Sent_updated = pd.DataFrame(df_Sent_updated_info)

# Creating four empty lists for the positive and negative tokens
# and the corresponding positive and negative polarity scores for the Word Clouds.
positive_pol = []
negative_pol = []
positive_pol_scores = []
negative_pol_scores = []

# Sentimentanalysis and collecting the polarity tokens and polarity scores
# Iterating over the index of the Dataframe in the column "text" and calling the SpaCy-Pipeline on it.
# Writing the Results of the Sentiment Analysis in the corresponding columns "created_at",
# "text" and "Polarity" of the Dataframe.
# Iterating over the SpaCy-Doc-Object and collecting the positive tokens and scores
# if the polarity is > 0 and writing them into the lists "positive_pol" and "positive_pol_scores"
# and collecting the negative tokens and scores if the polarity is < 0 and writing
# them into the lists "negative_pol" and "negative_pol_scores".
for index, sentence in df.iterrows():
    Sent = sentence.loc["text"]
    doc = nlp(Sent)
    df_Sent_updated.loc[index] = [sentence.loc["created_at"],sentence.loc["text"], float(doc._.blob.polarity)]
    for word in doc:
        if word._.blob.polarity > 0:
            positive_pol.append(word)
            positive_pol_scores.append(float(word._.blob.polarity))
        if word._.blob.polarity < 0:
            negative_pol.append(word)
            negative_pol_scores.append(float(word._.blob.polarity))

# Writing the positive tokens and positive scores into a new DataFrame
# Concatenating the two Dataframe into one Dataframe with the columns "positive token" and "positive score".
df_positive_pol = pd.DataFrame(positive_pol, columns=["positive token"])
df_positive_pol_scores = pd.DataFrame(positive_pol_scores, columns=["positive score"])
df_positive_concatenated = pd.concat([df_positive_pol, df_positive_pol_scores], axis="columns")

# Writing the negative tokens and negative scores into a new DataFrame
# Concatenating the two Dataframe into one Dataframe with the columns "negative token" and "negative score".
df_negative_pol = pd.DataFrame(negative_pol, columns=["negative token"])
df_negative_pol_scores = pd.DataFrame(negative_pol_scores, columns=["negative score"])
df_negative_concatenated = pd.concat([df_negative_pol, df_negative_pol_scores], axis="columns")

# Saving the Dataframe of the positive tokens and scores into your Directory as Excel.
new_file = os.path.join("Please enter filename.xlsx")
writer = pd.ExcelWriter(new_file)
df_positive_concatenated.to_excel(writer, sheet_name="Please enter filename.xlsx", index=False)
writer.close()

# Saving the Dataframe of the negative tokens and scores into your Directory as Excel.
new_file = os.path.join("Please enter filename.xlsx")
writer = pd.ExcelWriter(new_file)
df_negative_concatenated.to_excel(writer, sheet_name="Please enter filename.xlsx", index=False)
writer.close()

# Saving the Dataframe of the Results of the Sentiment Analysis as Excel.
new_file = os.path.join("Please enter filename.xlsx")
writer = pd.ExcelWriter(new_file)
df_Sent_updated.to_excel(writer, sheet_name="Please enter filename.xlsx", index=False)
writer.close()

# Reading the Excel-file with the results of the
# Sentiment Analysis and converting it into a CSV-file.
read_file = pd.read_excel("Please enter filename.xlsx")
read_file.to_csv("Please enter filename.csv", header=True)

# Converting the CSV-file into a Dataframe and parsing the date.
df = pd.read_csv("Please enter filename.csv", parse_dates=["created_at"])

# Creating three new Dataframes
# for each Polarity, positive, negative and neutral.
positive_polarity = df[df["Polarity"] > 0]
negative_polarity = df[df["Polarity"] < 0]
neutral = df[df["Polarity"] == 0]

# Printing the values
# Printing the average positive and negative polarity over the whole time frame.
print(positive_polarity.mean(numeric_only=True)["Polarity"])
print(negative_polarity.mean(numeric_only=True)["Polarity"])

# Printing the average positive and negative polarity over each month each year in the time frame.
print(positive_polarity.groupby([df["created_at"].dt.year, df["created_at"].dt.month])["Polarity"].mean())
print(negative_polarity.groupby([df["created_at"].dt.year, df["created_at"].dt.month])["Polarity"].mean())

# Counting the number of positive, negative and neutral Tweets over the year in the time frame.
print(positive_polarity.count()[0])
print(negative_polarity.count()[0])
print(neutral.count()[0])

# Counting the number of positive, negative and neutral Tweets over each month each year in the time frame.
print(positive_polarity.groupby([df["created_at"].dt.year, df["created_at"].dt.month]).count()["Polarity"])
print(negative_polarity.groupby([df["created_at"].dt.year, df["created_at"].dt.month]).count()["Polarity"])
print(neutral.groupby([df["created_at"].dt.year, df["created_at"].dt.month]).count()["Polarity"])
