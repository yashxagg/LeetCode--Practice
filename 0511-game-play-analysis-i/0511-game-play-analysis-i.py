import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Perform the grouping and find the minimum date
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    
    # Rename the column to 'first_login' as required by the problem
    result.rename(columns={'event_date': 'first_login'}, inplace=True)
    
    return result