import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Group by the required columns and count unique occurrences for the others
    result = daily_sales.groupby(['date_id', 'make_name']).agg({
        'lead_id': 'nunique',
        'partner_id': 'nunique'
    }).reset_index()
    
    # Rename columns to match the standard expected output
    result.columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners']
    
    return result