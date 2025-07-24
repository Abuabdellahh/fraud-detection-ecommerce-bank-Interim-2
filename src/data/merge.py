import pandas as pd

def ip_to_int(ip_str):
    parts = [int(x) for x in ip_str.split('.')]
    return (parts[0]<<24) + (parts[1]<<16) + (parts[2]<<8) + parts[3]

def merge_fraud_with_country(fraud_df, ip_country_df):
    fraud_df['ip_int'] = fraud_df['ip_address'].apply(ip_to_int)
    merged = pd.merge_asof(
        fraud_df.sort_values('ip_int'),
        ip_country_df.sort_values('lower_bound_ip_address'),
        left_on='ip_int',
        right_on='lower_bound_ip_address',
        direction='backward'
    )
    return merged
