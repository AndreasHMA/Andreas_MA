# Imports
from searchtweets import load_credentials, gen_request_parameters, ResultStream
import pandas as pd
import json

# Credential-Handling
# Loading credentials from the YAML-file from your Directory.
search_args = load_credentials(filename="./search_tweets_creds_example.yaml",
                               yaml_key="search_tweets_v2",
                               env_overwrite=False)

# Downloading Data
# Generating rule and search query with
# the required and desired parameters and operators.
rule = gen_request_parameters("vaccine covid (Moderna OR Pfizer OR AstraZeneca OR "
                              "JohnsonAndJohnson) lang:en (place_country:AU OR place_country:US OR "
                              "place_country:GB)-is:nullcast -is:retweet -is:quote",
                              start_time="2020-02-29",
                              end_time="2021-08-01",
                              tweet_fields="id,text,created_at,entities,lang,public_metrics",
                              expansions="geo.place_id",
                              place_fields="contained_within,country,country_code,full_name,geo,id,name,place_type",
                              results_per_call=500,
                              granularity=None)

# Calling the API-Endpoint
# and returning a stream of results
# with the help of the previously designed rules.
# Limiting the call to 30000 Tweets and max 100 pages.
rs = ResultStream(request_parameters=rule,
                  max_tweets=30000,
                  max_pages=100,
                  output_format="a",
                  **search_args)

# Creating the JSON-file,
# iterating over the ResultStream
# and dumping the Tweets into a JSON-file.
PRINT_AFTER_X = 100
with open("Test.json", "a", encoding="utf-8") as f:
    n = 0
    for tweet in rs.stream():
        n += 1
        if n % PRINT_AFTER_X == 0:
            print("{0}: {1}".format(str(n), tweet["created_at"]))
        json.dump(tweet, f)
        f.write('\n')
print("done")

# Opening the JSON-file from your Directory, appending the JSON to a list,
# normalizing the JSON-file into a Dataframe
# and saving it as a CSV-file.
tweets = []
for line in open("Test.json", "r"):
    tweets.append(json.loads(line))
df = pd.json_normalize(tweets, max_level=1)
df.to_csv("Please enter filename.csv", header=True, index=False)
