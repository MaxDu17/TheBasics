from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def generate_TSNE_points(embeddings, dims):
    tsne = TSNE(dims, verbose=1)
    tsne_proj = tsne.fit_transform(embeddings)
    return tsne_proj

def generate_PCA_points(embeddings, dims):
    pca = PCA(n_components=dims)
    pca.fit(embeddings)
    print(pca.explained_variance_ratio_)
    pca_proj = pca.transform(embeddings)
    return pca_proj