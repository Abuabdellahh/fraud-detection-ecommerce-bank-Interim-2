import pandas as pd

def clean_fraud_data(df):
    df = df.drop_duplicates()
    df = df.fillna(df.median(numeric_only=True))
    # Convert columns to appropriate types
    if 'signup_time' in df.columns:
        df['signup_time'] = pd.to_datetime(df['signup_time'])
    if 'purchase_time' in df.columns:
        df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    return df

def clean_creditcard_data(df):
    df = df.drop_duplicates()
    df = df.fillna(df.median(numeric_only=True))
    return df
