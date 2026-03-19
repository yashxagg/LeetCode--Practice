import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df_melted = products.melt(
        id_vars=['product_id'], 
        value_vars=['store1', 'store2', 'store3'],
        var_name='store', 
        value_name='price'
    )
    
    # Remove rows where the price is null (NaN)
    return df_melted.dropna(subset=['price'])   