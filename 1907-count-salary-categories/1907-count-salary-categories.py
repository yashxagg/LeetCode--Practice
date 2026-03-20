import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # 1. Define the categories and their logic
    # Low Salary: Income < 20000
    # Average Salary: 20000 <= Income <= 50000
    # High Salary: Income > 50000
    
    low_count = accounts[accounts['income'] < 20000].shape[0]
    avg_count = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)].shape[0]
    high_count = accounts[accounts['income'] > 50000].shape[0]
    
    # 2. Create the resulting DataFrame
    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_count, avg_count, high_count]
    })
    
    return result