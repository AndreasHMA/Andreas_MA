# !pip install spacy
# !pip install spacyTextblob
# !pip install en_core_web_lg
# !pandas
# !openpyxl
# !install emoji
# !contextualSpellCheck

# Imports
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
import os
import re
import emoji
import contextualSpellCheck

# Loading large english pipeline
#nlp = spacy.load("en_core_web_lg", exclude="parser, ner")

# Loading Tweets_dataframe
df = pd.read_csv("1_OG_Dataset.csv")
# print(df.columns)

#df_new = pd.DataFrame(df.drop(columns=
#        ["created_at", 'id', 'edit_history_tweet_ids', 'lang',
#       'entities.mentions', 'entities.annotations',
#       'public_metrics.retweet_count', 'public_metrics.reply_count',
#       'public_metrics.like_count', 'public_metrics.quote_count',
#       'geo.place_id', 'geo.country', 'geo.full_name', 'geo.id',
#       'entities.hashtags', 'entities.urls', 'entities.cashtags'],axis=1,inplace=False))
# print(df_new.columns)


#df_new["text"] = df_new["text"].str.replace(r'https?://[^ ]+', '', regex=True)
#df_new["text"] = df_new["text"].str.replace(r'@[^ ]+', '', regex=True)
#df_new["text"] = df_new["text"].str.replace(r'@ [^ ]+', '', regex=True)
#df_new["text"] = df_new["text"].str.replace(r'#[^ ]+', '', regex=True)
#df_new["text"] = df_new["text"].str.replace(r'&[^ ]+', '', regex=True)
#df_new["text"] = df_new["text"].str.replace(r'([A-Za-z])\1{2,}', r'\1', regex=True)
#df_new["text"] = emoji.demojize(df_new["text"], language="en")
#df_new["text"] = df_new["text"].str.replace(r'[^A-Za-z ]', '', regex=True)
#df_new["text"] = df_new["text"].apply(lambda x: " ".join(x.lower() for x in x.split()))

#nlp.Defaults.stop_words -= {"very", "such", "more", "really", "enough", "less", "top", "most", "same", "serious",
#                            "empty", "various", "down", "whole", "former", "few", "only", "first", "last"}

#sw_spacy = nlp.Defaults.stop_words
#print(sw_spacy)
#df_new["text"] = df_new["text"]\
#       .astype(str).apply(lambda x: " ".join(x for x in x.split() if x not in sw_spacy))

new_file = os.path.join("df_new.xlsx")
writer = pd.ExcelWriter(new_file)
df_new.to_excel(writer, sheet_name="df_new.xlsx", index=False)
writer.save()

# Preparing NlP-pipeline
# Creating and Adding textblob to pipeline
#nlp.add_pipe("contextual spellchecker")
#nlp.add_pipe("spacytextblob")

# Checking pipeline components
#pipe = nlp.component_names
#print(pipe)

# Sentiment analysis to get Polarity and Subjectivity and creating a new DataFrame
#df_Sent_updated_info = {"text": [], "Polartiy": [], "Subjectivity": []}
#df_Sent_updated = pd.DataFrame(df_Sent_updated_info)

#for index, sentence in df_new.iterrows():
#    Sent = sentence.loc["text"]
#    doc = nlp(Sent)
#    df_Sent_updated.loc[index] = [sentence.loc["text"], float(doc._.blob.polarity),doc._.blob.subjectivity]

# Saving new DataFrame as Excel
#new_file = os.path.join("df_Sent_updated.xlsx")
#writer = pd.ExcelWriter(new_file)
#df_Sent_updated.to_excel(writer, sheet_name="df_Sent_updated.xlsx", index=False)
#writer.save()

# Visualisierung
#


# !pip install spacy
# !pip install spacyTextblob
# !pip install en_core_web_lg
# !pandas

# Imports
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
import os

# Loading large english pipeline
nlp = spacy.load("en_core_web_lg")

# Loading Tweets_dataframe
df = pd.read_csv("Df_pruned.csv")
#print(df.columns)

df = pd.DataFrame(df.drop(columns=
        ['id', 'edit_history_tweet_ids', 'lang',
       'entities.mentions', 'entities.annotations',
       'public_metrics.retweet_count', 'public_metrics.reply_count',
       'public_metrics.like_count', 'public_metrics.quote_count',
       'geo.place_id', 'geo.country', 'geo.full_name', 'geo.id',
       'entities.hashtags', 'entities.urls', 'entities.cashtags'],axis=1,inplace=False))
#print(df.columns)

# Preparing our Text
# Noise removal and Stopword removal
df["text"] = df["text"].str.replace(r'https?://[^ ]+', '', regex=True).str.replace(r'@[^ ]+', '', regex=True)
df["text"] = df["text"].str.replace(r'@ [^ ]+', '', regex=True).str.replace(r'#[^ ]+', '', regex=True)
df["text"] = df["text"].str.replace(r'&amp[^ ]+', '', regex=True).str.replace(r'([A-Za-z])\1{2,}', r'\1', regex=True)
df["text"] = df["text"].apply(lambda x: " ".join(x.lower() for x in x.split()))

own_sw_list = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once",
"during", "out", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its",
"yours", "into", "of", "itself", "other", "off", "is", "s", "am", "or", "who",
"as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his",
"through", "don’", "nor", "me", "were", "her", "himself", "this", "should", "our", "their",
"while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them",
"and", "been", "have", "in", "will", "on", "yourselves", "then", "that", "because", "what", "over",
"why", "so", "can", "did", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "myself",
"which", "those", "i", "after", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it",
"how", "further", "was", "here", "than"]

from spacy.language import Language
@Language.component("stopword")
def stopword(doc):
    for token in doc:
        token = [token for token in doc if token.text not in own_sw_list]
        print(token)
    return doc
nlp.add_pipe("stopword", after = "ner")
#token for token in about_doc if not token.is_stop]
df["text"] = df["text"].astype(str).apply(lambda x: " ".join(x for x in x.split() if x not in own_sw_list))

#df["text"] = df["text"].apply(doc_cleaner)
#print(df["text"])

#nlp.add_pipe("stopword", after = "ner")

# Preparing NlP-pipeline
# Creating and Adding textblob to pipeline
nlp.add_pipe("spacytextblob")

# Checking pipeline components
pipe = nlp.component_names
print(pipe)

# Sentiment analysis to get Polarity and Subjectivity and creating a new DataFrame
df_Sent_updated_info = {"created_at": [], "text": [], "Polarity": []}
df_Sent_updated = pd.DataFrame(df_Sent_updated_info)

for index, sentence in df.iterrows():
    Sent = sentence.loc["text"]
    doc = nlp(Sent)
    print(doc)
    df_Sent_updated.loc[index] = [sentence.loc["created_at"],sentence.loc["text"], float(doc._.blob.polarity)]

# Saving new DataFrame as Excel
new_file = os.path.join("df_Sent_updated.xlsx")
writer = pd.ExcelWriter(new_file)
df_Sent_updated.to_excel(writer, sheet_name="df_Sent_updated.xlsx", index=False)
writer.save()

# Reading an excel file
read_file = pd.read_excel("df_Sent_updated.xlsx")
read_file.to_csv("df_Sent_updated.csv", index=None, header=True)

postive_pol = []
negative_pol = []

for index, word in df.iterrows():
    Sent = word.loc["text"]
    doc = nlp(Sent)
    for word in doc:
        if word._.blob.polarity > 0:
            postive_pol.append(word)
        if word._.blob.polarity < 0:
            negative_pol.append(word)

print(postive_pol)
print(negative_pol)