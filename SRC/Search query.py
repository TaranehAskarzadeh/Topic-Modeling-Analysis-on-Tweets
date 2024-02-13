# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:13:25 2024

@author: Taraneh
"""

from searchtweets import ResultStream, gen_rule_payload, load_credentials


# Make sure you have created a 'twitter_keys.yaml' file with your credentials
twitter_keys = {
    'search_tweets_api': {
        'account_type': 'premium',  # or 'standard' based on your access level
        'endpoint': 'https://api.twitter.com/1.1/tweets/search/fullarchive/your_dev_env_name.json',  # replace with your endpoint
        'consumer_key': 'YOUR_CONSUMER_KEY',
        'consumer_secret': 'YOUR_CONSUMER_SECRET',
        'access_token': 'YOUR_ACCESS_TOKEN',
        'access_token_secret': 'YOUR_ACCESS_TOKEN_SECRET'
    }
}

# Load credentials 
search_args = load_credentials("twitter_keys.yaml", yaml_key="search_tweets_api", env_overwrite=False)

# Define the search query
query = "(#covid19 OR #coronavirus OR #pandemic OR #covid OR #corona OR #spread " \
        "OR #virus) AND (#publictransportation OR #publictransit OR #bike OR " \
        "#bus OR #metro OR #bikeshare OR #scootershare OR #masstransit OR " \
        "#subway OR #scooter OR #uber OR #lyft OR #flight OR #airline " \
        "OR #carpool OR #riders) lang:en -is:retweet"

# Generate the rule payload for the search
rule = gen_rule_payload(query, results_per_call=100)  # adjust the results per call as needed

# Use ResultStream to get the tweets
tweets = ResultStream(rule_payload=rule,
                      max_results=100,  # adjust the max number of results as needed
                      **search_args)

for tweet in tweets.stream():
    print(tweet)

