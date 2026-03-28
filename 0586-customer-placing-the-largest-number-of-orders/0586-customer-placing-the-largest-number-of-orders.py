import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Handle empty DataFrame case
    if orders.empty:
        return pd.DataFrame({'customer_number': []})
    
    # Use mode() to find the most frequent customer_number
    # Since the problem guarantees exactly one top customer, 
    # mode() will return a Series with that single value at index 0.
    top_customer = orders['customer_number'].mode().to_frame()
    
    return top_customer  