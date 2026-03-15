import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # This line must be 4 spaces in
    invalid_mask = tweets['content'].str.len() > 15
    
    # This line must be exactly aligned with the one above
    return tweets[invalid_mask][['tweet_id']]