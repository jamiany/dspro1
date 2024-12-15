import pandas as pd
from sklearn.decomposition import PCA


def pca(df):
    res = PCA(n_components=2)
    principal_components = res.fit_transform(df)

    return pd.DataFrame(principal_components, columns=['PC1', 'PC2'])
