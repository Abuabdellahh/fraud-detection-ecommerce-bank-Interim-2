import pandas as pd

def load_fraud_data(path):
    """Load the e-commerce fraud data CSV."""
    return pd.read_csv(path)

def load_creditcard_data(path):
    """Load the credit card fraud data CSV."""
    return pd.read_csv(path)

def load_ip_country_data(path):
    """Load the IP address to country mapping CSV."""
    return pd.read_csv(path)
