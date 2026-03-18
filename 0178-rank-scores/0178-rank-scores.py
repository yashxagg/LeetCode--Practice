import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # 1. Sort by score in descending order
    scores = scores.sort_values(by='score', ascending=False)
    
    # 2. Calculate the rank using the 'dense' method
    # This ensures ties get the same rank and no numbers are skipped
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    
    # 3. Return only the score and rank columns as per typical requirements
    return scores[['score', 'rank']]