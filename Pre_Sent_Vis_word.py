# !pip install spacy
# !pip install spacyTextblob
# !pip install en_core_web_lg
# !pandas
# !matplotlib
# !WordCloud

# Imports
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
import os

# Loading Tweets_dataframe
df = pd.read_csv("DF_Pfizer.csv")

# Preparing our Text
# Noise removal and Stopword removal
df["text"] = df["text"].str.replace(r'https?://[^ ]+', '', regex=True).str.replace(r'@[^ ]+', '', regex=True)
df["text"] = df["text"].str.replace(r'@ [^ ]+', '', regex=True).str.replace(r'#[^ ]+', '', regex=True)
df["text"] = df["text"].str.replace(r'&amp[^ ]+', '', regex=True).str.replace(r'([A-Za-z])\1{2,}', r'\1', regex=True)
df["text"] = df["text"].apply(lambda x: " ".join(x.lower() for x in x.split()))

# Loading large english pipeline
nlp = spacy.load("en_core_web_lg")

# Preparing NlP-pipeline
# Creating and Adding textblob to pipeline
nlp.add_pipe("spacytextblob")

# Checking pipeline components
pipe = nlp.component_names
print(pipe)

# Sentiment analysis to get Polarity and Subjectivity and creating a new DataFrame
df_Sent_updated_info = {"created_at": [], "text": [], "Polarity": []}
df_Sent_updated = pd.DataFrame(df_Sent_updated_info)

# Creating two empty list for tokens with polarity scores
postive_pol = []
negative_pol = []
positive_pol_scores = []
negative_pol_scores = []

# Sentimentanalysis and collecting tokens with polarity's
for index, sentence in df.iterrows():
    Sent = sentence.loc["text"]
    doc = nlp(Sent)
    df_Sent_updated.loc[index] = [sentence.loc["created_at"],sentence.loc["text"], float(doc._.blob.polarity)]
    for word in doc:
        if word._.blob.polarity > 0:
            postive_pol.append(word)
            positive_pol_scores.append(float(word._.blob.polarity))
        if word._.blob.polarity < 0:
            negative_pol.append(word)
            negative_pol_scores.append(float(word._.blob.polarity))

df_positve_pol = pd.DataFrame(postive_pol, columns = ['positive token'])
df_positve_pol_scores = pd.DataFrame(positive_pol_scores, columns = ['positive score'])
df_positve_concatenated = pd.concat([df_positve_pol, df_positve_pol_scores ], axis="columns")

df_negative_pol = pd.DataFrame(negative_pol, columns = ['negative token'])
df_negative_pol_scores = pd.DataFrame(negative_pol_scores, columns = ['negative score'])
df_negative_concatenated = pd.concat([df_negative_pol, df_negative_pol_scores ], axis="columns")

# Saving new DataFrame as Excel
new_file = os.path.join("df_Sent_updated.xlsx")
writer = pd.ExcelWriter(new_file)
df_Sent_updated.to_excel(writer, sheet_name="df_Sent_updated.xlsx", index=False)
writer.save()

read_file = pd.read_excel("df_Sent_updated.xlsx")
read_file.to_csv("df_Sent_updated.csv", index=None, header=True)

# Converting Excel to Dataframe
df = pd.read_csv("df_Sent_updated.csv", parse_dates=["created_at"])

# Creating new Dataframe with positive, negative and neutral Polarity
positive_polarity = df[df["Polarity"] > 0]
negative_polarity = df[df["Polarity"] < 0]
neutral = df[df["Polarity"] == 0]

# printing the average positive and negative polarity over the year
print(positive_polarity.mean()["Polarity"])
print(negative_polarity.mean()["Polarity"])

# printing the average positive and negative polarity over each month
print(positive_polarity.groupby([df["created_at"].dt.year, df["created_at"].dt.month])["Polarity"].mean())
print(negative_polarity.groupby([df["created_at"].dt.year, df["created_at"].dt.month])["Polarity"].mean())

#print(positive_polarity.groupby([df["created_at"].dt.year, df["created_at"].dt.month])["Polarity"].mean())
# print(negative_polarity.groupby(df["created_at"].dt.month)["Polarity"].mean())
# counting the number of positive, negative and neutral Tweets over the year
print(positive_polarity.count()[0])
print(negative_polarity.count()[0])
print(neutral.count()[0])

# counting the number of positive, negative and neutral Tweets over each month
print(positive_polarity.groupby([df["created_at"].dt.year, df["created_at"].dt.month]).count()["Polarity"])
print(negative_polarity.groupby([df["created_at"].dt.year, df["created_at"].dt.month]).count()["Polarity"])
print(neutral.groupby([df["created_at"].dt.year, df["created_at"].dt.month]).count()["Polarity"])

