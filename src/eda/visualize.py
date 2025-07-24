import matplotlib.pyplot as plt
import seaborn as sns

def plot_univariate(df, column):
    plt.figure(figsize=(8,4))
    sns.histplot(df[column], kde=True)
    plt.title(f'Univariate Analysis: {column}')
    plt.show()

def plot_bivariate(df, col1, col2):
    plt.figure(figsize=(8,4))
    sns.boxplot(x=df[col1], y=df[col2])
    plt.title(f'Bivariate Analysis: {col1} vs {col2}')
    plt.show()
