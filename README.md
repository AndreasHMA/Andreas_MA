# The Vaccination Discussion during the COVID-19 Pandemic

## Introduction

This project was developed as part of a master's thesis for the degree of Masters of Arts in Digital Humanities at the University of Basel. The title of the thesis is: The Vaccination Discussion during the COVID-19 Pandemic. A sentiment analysis.

The goal is to analyze tweets based on their sentiment, or the polarity of them, using the methodology of sentiment analysis. In doing so, the most positive frequent and most negative frequent words are also analyzed using *Word Clouds* and finally, the numerical distribution of tweets is also presented into a geographical perspective using the *Bubble Map*.  

The task of the actual codes is to download tweets related to the defined search parameters, to check them according to certain criteria or based on questions and filter them accordingly. By applying the sentiment analysis the Tweets are analysed and the desired values are presented. During the sentiment analysis, the positive and negative words and the corresponding polarity values are also collected and saved, followed by a visualization in the *WordCloud* code. In a different step, the tweets can also be prepared for the subsequent visualization with the *Bubble map* using the *Dataframe processing* code.

As these programs all belong together, they have also to run in the following order to get the desired result:

*TweetSearch + search_tweets_creds_example*

*Deleting Duplicates*

*Data filtering*

*SentimentAnalysis*

*WordCloud*

*Data processing + Bubble Map*

## Requirements

The codes mentioned above have mostly in common the similar components and requirements. Hence in the following all necessary programs, installations and/or modules or packages and the corresponding versions of these are represented once and apply to all following codes and the further presentation.The programs, installations and/or modules are downloaded either directly from the webside of the respective manufacturers or depending upon availability of the modules with the help of the Anaconda navigator or Python packages. The list below shows the actual versions used during the project. These were the most recent versions at that point in time. Also, some modules only run with certain Anaconda, Pycharm or even Python versions and therefore differ from the current version. The following components and versions are applied:

Anaconda Navigator/ Distribution 	2.3.2 https://www.anaconda.com/ 

Windows 10 64-Bit Version

Pycharm Professional	2022.03

Python	3.9 64-Bit Version

Pandas	1.5.2

Searchtweets-v2	1.1.1

OS	3.9

regex	2022.10.31

SpaCy	3.3.1

SpaCyTextBlob	4.0

SpaCy-model-en_core_web_lg	3.3.0

WordCloud	1.8.2.2

Mathplotlib	3.6.2

GeoPy	2.3.0

Plotly	5.9.0

# Individual Codes

As already shown, Pycharm or Python is used via the Anaconda Navigator and accordingly these are also installed with or via Anaconda. In general, it is recommended to download and copy all programs into a single Python project, because this way not only the installations are shared between the programs, but also the inputs and outputs can be used in parallel and all required components are located in one directory. The programs are in such a way adjusted taking the input and the output always from the current project and/or the current Directory and/or the location of the programs. This simplifies the handling substantially. 
The names of the files of the input and output have to be inserted in the respective line of the code. The exact line and location is marked with the following sentence: *Please enter filename*. If necessary, also depending on the code for example, the titles have to be changed. This is usually also in connection with: *Please enter..*.Finally, it should be noted that the description of the codes or the lines is also present in the code itself in detailed form. Also the properties and/or the changed parameters of the respective codes are listed briefly. The meaning of these is to be taken from the respective documentation of the modules resp. the most important parameters are more defined also in the chapter methodology in the work mentioned above. However, most of these are self-explanatory or only visual in nature and can therefore be set according to one's own preferences. For further context and literature you can also check the Bibliography.

## *TweetSearch and search_tweets_creds_example*

The programs *TweetSearch* and *search_tweets_creds_example* are to be used together. *Search_tweets_creds_example* provides the authentication keys and the endpoint to Twitter. For the application, a *Twitter Developer Account* with *Academic Research Access* and corresponding keys and tokens must be available. These must then be copied into *search_tweets_creds_example* at the appropriate places. The YAML file does not take any input except the keys and tokens already outlined, and in that sense does not present any output directly. 
Therefore, the *TweetSearch* program does not take any direct input from the directory. However, the YAML file must be in the same Directory as it provides the authentication. In summary, the program takes the authentication codes and, using them and search parameters set in that code, retrieves tweets, returns them to the user, and finally saves them as a JSON file or converts and saves the code. In this sense the output is a JSON, which is not interesting for further codes, and a CSV file. The downloaded tweets are now in this file on the basis of the set search parameters. These will be further used in the next steps.


## *Deleting Duplicates*

The code *Deleting Duplicates* takes a CSV file and removes duplicates based on the *text* column in the dataframe. Hereby the first entry of the duplicate will be kept. It is intended that the CSV file is taken from the *SearchTweets* code. The output here is an Excel file. In the next steps we will only work with Excel files in the in- and output. 


## *Data filtering*

The code *Data filtering* is used comprehensivly to filter the data according to certain criteria. Hereby the Excel file from the code *Deleting Duplicates* should be filtered according to the desired criteria depending on the question setup. Again, this takes an Excel file and delivers an Excel file.


## *SentimentAnalysis*

Now to the central step of the sentiment analysis in the name-giving code *SentimentAnalysis*. This code takes an Excel file as input. This should come from the code *data filtering*. The code processes and analyzes with the help of *SpaCy*, the big English pipeline *en_core_web_lg* and *SpaCyTextBlob* the passed file respectively the column *text*. The output of the program is manifold. On one side the output of the sentiment analysis itself is stored in an Excel file. On the other side, two Excel files containing the positive and negative words resp. their corresponding polarity values analyzed in the sentiment analysis are created. These two Excel files are needed for the later *WordCloud*. Subsequently, the Excel file with the result of the sentiment analysis is entered again, converted into a CSV, rewritten into a data frame and finally divided into three data frames according to the *Polarity* column, i.e. according to the polarity values. With the help of these, the number of positive, negative and neutral tweets in a given period, the average positive and negative polarity in a given period, the number of positive, negative and neutral tweets per month in a given period and finally the average positive and negative polarity per month in a given period are delivered.


## *WordCloud*

The following code visualizes the two *Word Clouds*. The two Excel files delivered in the previous step, which contain the positive and negative polarity carriers as well as the positive and negative polarity values, are inserted here as input and converted into two data frames and finally converted into a Sting. Finally two Word Clouds, one for the positive words and one for the negative terms are visualized and saved as JPG. 


## *Data processing* and *Bubble map*

The code *Data processing* takes over the Excel file created from the code *Data filtering*. The code described here represents the preliminary work for the *Bubble map*. The *Bubble map* needs longitude, latitude and a count value to be able to work. Important to note that the column *geo.country* must be translated into English, otherwise *GeoPy* will not recognize the country. Using *GeoPy*, the code adds the longitude and latitude to the respective tweets, counts the unique values based on the geographic address, and deletes the duplicates. This process may take some time due to the required limitation of calls. It may also be necessary to split files with many entries as they are too large. The output is now an Excel file, which is used again in the Code *Bubble Map* in the form of the input. However, this Excel file must be edited manually beforehand. The table has to be sorted in descending order according to the values in the *count* column. In addition the first row between the headers and the individual entries must be left blank. It may also be possible that the row *count* has slipped slightly downwards and this has to be adjusted accordingly. However, the values always correspond to the entries. As a first step the default settings are made by setting the important limits, the labels and the colors. Then the bubble map is already created and delivered. This opens in the Internet browser and can be downloaded from there and saved via screenshot.

