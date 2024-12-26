import plotly.express as px
from matplotlib import pyplot as plt
import seaborn as sns


def scatter(df, names = [], interactive: bool = False):
    if interactive:
        fig = px.scatter(df, x='PC1', y='PC2')
        fig.update_traces(
            text=names,
            hovertemplate='%{text}',
            mode='markers'
        )
        fig.show()
    else:
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=df, x='PC1', y='PC2', hue='personal_cluster', palette='tab10', s=100)
        plt.title('K-Means Clustering')
        plt.show()
