import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # 1. Get unique salaries and sort them descending
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # 2. Check if N is valid (N-th exists) and N > 0
    if N <= 0 or len(unique_salaries) < N:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # 3. Use iloc to get the (N-1)-th index (since pandas is 0-indexed)
    nth_highest = unique_salaries.iloc[N - 1]
    
    # 4. Return as a DataFrame with the specific column name expected
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})