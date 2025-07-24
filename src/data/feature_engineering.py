import pandas as pd

def add_time_features(df):
    if 'purchase_time' in df.columns:
        df['hour_of_day'] = df['purchase_time'].dt.hour
        df['day_of_week'] = df['purchase_time'].dt.dayofweek
    if 'signup_time' in df.columns and 'purchase_time' in df.columns:
        df['time_since_signup'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds() / 3600.0
    return df

def add_transaction_frequency(df):
    if 'user_id' in df.columns and 'purchase_time' in df.columns:
        df = df.sort_values(['user_id', 'purchase_time'])
        df['transaction_count'] = df.groupby('user_id').cumcount() + 1
        df['time_diff'] = df.groupby('user_id')['purchase_time'].diff().dt.total_seconds().fillna(0)
    return df
