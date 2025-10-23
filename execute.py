import pandas as pd

def main():
    # Read data from CSV
    df = pd.read_csv('data.csv')

    # Validate dataframe has 'product' and 'revenew' (fix typo here)
    # Suppose it should be 'revenue' (standard spelling)
    if 'product' not in df.columns or 'revenue' not in df.columns:
        raise ValueError("Missing required columns")

    # Compute total revenue per product
    result_df = df.groupby('product')['revenue'].sum().reset_index()

    # Return result as JSON string
    result_json = result_df.to_json(orient='records')
    return result_json

if __name__ == "__main__":
    print(main())
